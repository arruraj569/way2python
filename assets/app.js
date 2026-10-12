(() => {
  'use strict';
  const catalog = window.WAY2PYTHON_LESSONS || [];
  const ids = new Set(catalog.map(lesson => lesson.id));
  const key = 'way2python:learning:v1';
  let storageWorks = true;
  let timer;
  const empty = () => ({version: 1, saved: [], completed: []});
  function clean(value) {
    if (!value || value.version !== 1 || !Array.isArray(value.saved) || !Array.isArray(value.completed)) {
      throw new Error('Choose a Way2Python progress export (version 1).');
    }
    return {version: 1, saved: [...new Set(value.saved.filter(id => ids.has(id)))],
      completed: [...new Set(value.completed.filter(id => ids.has(id)))]};
  }
  let state = empty();
  try {
    const raw = localStorage.getItem(key);
    if (raw) state = clean(JSON.parse(raw));
  } catch (_) { storageWorks = false; }
  function toast(message) {
    const element = document.querySelector('.toast');
    if (!element) return;
    element.textContent = message;
    element.classList.add('visible');
    clearTimeout(timer);
    timer = setTimeout(() => element.classList.remove('visible'), 4000);
  }
  function persist() {
    try { localStorage.setItem(key, JSON.stringify({...state, updatedAt: new Date().toISOString()})); }
    catch (_) { storageWorks = false; }
    renderState();
  }
  function renderState() {
    document.querySelectorAll('[data-save]').forEach(button => {
      const saved = state.saved.includes(button.dataset.save);
      button.setAttribute('aria-pressed', String(saved));
      const lesson = catalog.find(item => item.id === button.dataset.save);
      button.setAttribute('aria-label', `${saved ? 'Unsave' : 'Save'} ${lesson?.title || 'lesson'}`);
      button.textContent = button.classList.contains('save-button') ? (saved ? '♥' : '♡') : (saved ? '♥ Lesson saved' : '♡ Save lesson');
    });
    document.querySelectorAll('[data-complete]').forEach(button => {
      const complete = state.completed.includes(button.dataset.complete);
      button.setAttribute('aria-pressed', String(complete));
      button.textContent = complete ? 'Completed ✓' : 'Mark complete ✓';
    });
    document.querySelectorAll('[data-complete-label]').forEach(label => {
      label.textContent = state.completed.includes(label.dataset.completeLabel) ? '✓ Completed' : '';
    });
    document.querySelectorAll('[data-saved]').forEach(label => label.textContent = state.saved.length);
    document.querySelectorAll('[data-progress]').forEach(label => label.textContent = `${state.completed.length} lesson${state.completed.length===1 ? '' : 's'} completed`);
    document.querySelectorAll('[data-progress-title]').forEach(label => label.textContent = `${state.completed.length} of ${catalog.length} lessons complete`);
    document.querySelectorAll('[data-progress-bar]').forEach(bar => {bar.max = catalog.length; bar.value = state.completed.length;});
    document.querySelectorAll('[data-progress-percent]').forEach(label => label.textContent = `${Math.round(state.completed.length / Math.max(1,catalog.length) * 100)}%`);
    document.querySelectorAll('[data-milestone-ids]').forEach(element => {
      const groupIds = JSON.parse(element.dataset.milestoneIds);
      const complete = groupIds.filter(id => state.completed.includes(id)).length;
      element.querySelector('.milestone-progress').textContent = `${complete} of ${groupIds.length} lessons complete`;
    });
    if (document.getElementById('library-search')) filterLibrary(false);
  }
  document.querySelectorAll('[data-save]').forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.save;
    if (!ids.has(id)) return;
    const saved = state.saved.includes(id);
    state.saved = saved ? state.saved.filter(value => value !== id) : [...state.saved,id];
    persist();
    toast(storageWorks ? (saved ? 'Lesson removed from saved lessons.' : 'Lesson saved. Find it in Saved lessons.') : 'Updated for this page. Browser storage is unavailable; export your progress to keep it.');
  }));
  document.querySelectorAll('[data-complete]').forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.complete;
    if (!ids.has(id)) return;
    const completed = state.completed.includes(id);
    state.completed = completed ? state.completed.filter(value => value !== id) : [...state.completed,id];
    persist();
    toast(storageWorks ? (completed ? 'Marked as still to learn.' : 'Lesson complete. Keep building!') : 'Updated for this page. Export your progress to keep it.');
  }));
  window.addEventListener('storage', event => {
    if (event.key !== key) return;
    try { state = event.newValue ? clean(JSON.parse(event.newValue)) : empty(); renderState(); } catch (_) {}
  });
  const menu = document.querySelector('.menu-toggle');
  const sidebar = document.getElementById('sidebar');
  function syncHashNavigation() {
    if (document.body.dataset.page !== 'home') return;
    const topic = location.hash === '#topic-index';
    const homeLink = document.querySelector('.nav-link[href="index.html"]');
    const indexLink = document.querySelector('.nav-link[href="index.html#topic-index"]');
    [homeLink,indexLink].forEach(link => link?.removeAttribute('aria-current'));
    homeLink?.classList.toggle('active',!topic);
    indexLink?.classList.toggle('active',topic);
    (topic ? indexLink : homeLink)?.setAttribute('aria-current','page');
  }
  window.addEventListener('hashchange',syncHashNavigation);
  syncHashNavigation();
  function closeMenu() {sidebar?.classList.remove('open'); menu?.setAttribute('aria-expanded','false');}
  menu?.addEventListener('click', () => {
    const open = sidebar.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(open));
  });
  document.addEventListener('click', event => {
    if (sidebar?.classList.contains('open') && !sidebar.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu();
    if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable) return;
    event.preventDefault();
    const search = document.getElementById('library-search') || document.getElementById('index-search');
    if (search) search.focus();
    else window.location.href = `${document.body.dataset.root}library.html?focus=1`;
  });
  document.querySelectorAll('.copy-code').forEach(button => button.addEventListener('click', async () => {
    const value = button.closest('.code-block').querySelector('code').textContent;
    try {
      if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(value);
      else {
        const field = document.createElement('textarea');
        field.value = value; field.className = 'visually-hidden'; document.body.appendChild(field);
        field.select(); const success = document.execCommand('copy'); field.remove();
        if (!success) throw new Error('Copy failed');
      }
      button.textContent = 'Copied ✓'; toast('Code copied.');
      setTimeout(() => button.textContent = 'Copy code', 2000);
    } catch (_) {toast('Copy is unavailable. Select the code to copy it manually.');}
  }));
  const indexSearch = document.getElementById('index-search');
  const indexGroup = document.getElementById('index-group');
  function filterIndex() {
    const words = indexSearch.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const group = indexGroup.value;
    let collections = 0, lessons = 0;
    document.querySelectorAll('.index-group').forEach(section => {
      let visibleCards = 0;
      section.querySelectorAll('.index-topic').forEach(card => {
        let visibleLessons = 0;
        card.querySelectorAll('[data-index-lesson]').forEach(row => {
          const match = (!group || section.dataset.indexGroup === group) && words.every(word => (`${card.dataset.collection} ${row.dataset.search}`).includes(word));
          row.hidden = !match;
          if (match) visibleLessons++;
        });
        card.hidden = visibleLessons === 0;
        const details = card.querySelector('details');
        if (details) {
          const count = [...details.querySelectorAll('li')].filter(row => !row.hidden).length;
          details.open = words.length > 0;
          details.hidden = count === 0;
          details.querySelector('summary').textContent = `${count} ${words.length ? 'matching' : 'more'} lesson${count === 1 ? '' : 's'}`;
        }
        if (visibleLessons) {visibleCards++; collections++; lessons += visibleLessons;}
      });
      section.hidden = visibleCards === 0;
    });
    document.getElementById('index-count').textContent = `${collections} collection${collections === 1 ? '' : 's'} · ${lessons} lesson${lessons === 1 ? '' : 's'}`;
    document.getElementById('index-empty').hidden = lessons !== 0;
  }
  indexSearch?.addEventListener('input',filterIndex);
  indexGroup?.addEventListener('change',filterIndex);
  document.getElementById('index-clear')?.addEventListener('click',() => {indexSearch.value = ''; indexGroup.value = ''; filterIndex(); indexSearch.focus();});
  let collection = '';
  const librarySearch = document.getElementById('library-search');
  const libraryGroup = document.getElementById('library-group');
  const libraryLevel = document.getElementById('library-level');
  const libraryShow = document.getElementById('library-show');
  function filterLibrary(updateUrl = true) {
    const words = librarySearch.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    document.querySelectorAll('.lesson-card').forEach(card => {
      const id = card.dataset.lesson;
      const showMatch = !libraryShow.value || (libraryShow.value === 'saved' && state.saved.includes(id)) || (libraryShow.value === 'complete' && state.completed.includes(id)) || (libraryShow.value === 'incomplete' && !state.completed.includes(id));
      const match = words.every(word => card.dataset.search.includes(word)) && (!libraryGroup.value || card.dataset.group === libraryGroup.value) && (!libraryLevel.value || card.dataset.level === libraryLevel.value) && (!collection || card.dataset.collection === collection) && showMatch;
      card.hidden = !match;
      if (match) count++;
    });
    document.getElementById('library-count').textContent = `${count} lesson${count === 1 ? '' : 's'}${libraryShow.value === 'saved' ? ' saved' : ''}`;
    document.getElementById('library-empty').hidden = count !== 0;
    const filterLabel = document.getElementById('collection-filter');
    filterLabel.hidden = !collection;
    filterLabel.textContent = collection ? `Collection: ${collection} · Use Clear filters to explore everything.` : '';
    const savedNav = document.querySelector('.nav-link[href$="library.html?saved=1"]');
    const libraryNav = document.querySelector('.nav-link[href$="library.html"]');
    [savedNav,libraryNav].forEach(link => link?.removeAttribute('aria-current'));
    savedNav?.classList.toggle('active',libraryShow.value === 'saved');
    libraryNav?.classList.toggle('active',libraryShow.value !== 'saved');
    (libraryShow.value === 'saved' ? savedNav : libraryNav)?.setAttribute('aria-current','page');
    const crumb = document.querySelector('.crumb-label');
    if (crumb) crumb.textContent = libraryShow.value === 'saved' ? 'Saved lessons' : 'All lessons';
    if (updateUrl) {
      const params = new URLSearchParams();
      if (librarySearch.value.trim()) params.set('q',librarySearch.value.trim());
      if (libraryGroup.value) params.set('group',libraryGroup.value);
      if (libraryLevel.value) params.set('level',libraryLevel.value);
      if (libraryShow.value === 'saved') params.set('saved','1');
      else if (libraryShow.value) params.set('show',libraryShow.value);
      if (collection) params.set('collection',collection);
      history.replaceState(null,'',`${location.pathname}${params.size ? `?${params}` : ''}`);
    }
  }
  function clearLibrary() {
    librarySearch.value = ''; libraryGroup.value = ''; libraryLevel.value = ''; libraryShow.value = ''; collection = '';
    filterLibrary(); librarySearch.focus();
  }
  if (librarySearch) {
    const params = new URLSearchParams(location.search);
    librarySearch.value = params.get('q') || '';
    libraryGroup.value = params.get('group') || '';
    libraryLevel.value = params.get('level') || '';
    libraryShow.value = params.get('saved') === '1' ? 'saved' : params.get('show') || '';
    collection = params.get('collection') || '';
    librarySearch.addEventListener('input',() => filterLibrary());
    [libraryGroup,libraryLevel,libraryShow].forEach(control => control.addEventListener('change',() => filterLibrary()));
    document.getElementById('library-search-form').addEventListener('submit',event => {event.preventDefault(); filterLibrary();});
    document.getElementById('library-clear').addEventListener('click',clearLibrary);
    document.querySelectorAll('[data-clear-library]').forEach(button => button.addEventListener('click',clearLibrary));
    filterLibrary(false);
    if (params.get('focus') === '1') librarySearch.focus();
  }
  function downloadJson(value, name) {
    const objectUrl = URL.createObjectURL(new Blob([JSON.stringify(value,null,2)],{type:'application/json'}));
    const link = document.createElement('a'); link.href = objectUrl; link.download = name;
    document.body.appendChild(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(objectUrl),1000);
  }
  document.getElementById('export-progress')?.addEventListener('click',() => {
    downloadJson({...state, exportedAt:new Date().toISOString()},'way2python-progress.json');
    toast('Progress exported. Keep the file to import it later.');
  });
  document.getElementById('import-progress')?.addEventListener('change', async event => {
    const file = event.target.files[0]; if (!file) return;
    try {
      if (file.size > 2000000) throw new Error('Choose a progress file smaller than 2 MB.');
      const imported = clean(JSON.parse(await file.text()));
      state = {version:1,saved:[...new Set([...state.saved,...imported.saved])],completed:[...new Set([...state.completed,...imported.completed])]};
      persist(); toast('Progress imported and merged with your current progress.');
    } catch (error) {toast(error.message || 'Could not read that progress file.');}
    event.target.value = '';
  });
  if (indexSearch) filterIndex();
  const interviewSearch = document.getElementById('interview-search');
  const interviewGroup = document.getElementById('interview-group');
  function filterInterviews() {
    const words = interviewSearch.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count=0;
    document.querySelectorAll('.interview-card').forEach(card=>{
      const match=(!interviewGroup.value || card.dataset.interviewGroup===interviewGroup.value) && words.every(word=>card.dataset.search.includes(word));
      card.hidden=!match;
      if(match)count++;
    });
    document.getElementById('interview-count').textContent=`${count} interview topic${count===1?'':'s'}`;
    document.getElementById('interview-empty').hidden=count!==0;
  }
  if(interviewSearch){
    interviewSearch.addEventListener('input',filterInterviews);
    interviewGroup.addEventListener('change',filterInterviews);
    document.getElementById('interview-clear').addEventListener('click',()=>{interviewSearch.value='';interviewGroup.value='';filterInterviews();interviewSearch.focus();});
  }
  const patternSearch = document.getElementById('pattern-search');
  if (patternSearch) {
    const category = document.getElementById('pattern-category');
    const priority = document.getElementById('pattern-priority');
    function filterPatterns() {
      const words = patternSearch.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      let count = 0;
      document.querySelectorAll('.pattern-card').forEach(card => {
        const match = (!category.value || card.dataset.category === category.value)
          && (!priority.value || card.dataset.priority === priority.value)
          && words.every(word => card.dataset.search.includes(word));
        card.hidden = !match;
        if (match) count++;
      });
      document.getElementById('pattern-count').textContent = `${count} design-pattern topic${count === 1 ? '' : 's'}`;
      document.getElementById('pattern-empty').hidden = count !== 0;
    }
    patternSearch.addEventListener('input', filterPatterns);
    category.addEventListener('change', filterPatterns);
    priority.addEventListener('change', filterPatterns);
    document.getElementById('pattern-clear').addEventListener('click', () => {
      patternSearch.value = ''; category.value = ''; priority.value = '';
      filterPatterns(); patternSearch.focus();
    });
  }
  renderState();
})();
