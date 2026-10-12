(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  let loginAttempt = 0;
  byId('login-form').addEventListener('submit', event => {
    event.preventDefault();
    const attempt = ++loginAttempt;
    const email = byId('email').value.trim(), password = byId('password').value;
    const button = event.currentTarget.querySelector('[type=submit]');
    button.disabled = true;
    byId('login-status').textContent = 'Signing in…';
    setTimeout(() => {
      if (attempt !== loginAttempt) return;
      byId('login-status').textContent = email === 'learner@example.test' && password === 'python123' ? 'Welcome, learner!' : 'Invalid credentials';
      button.disabled = false;
    }, 300);
  });
  byId('sign-out').addEventListener('click', () => {
    loginAttempt++;
    byId('login-status').textContent = 'Not signed in';
    byId('login-form').querySelector('[type=submit]').disabled = false;
    byId('password').value = '';
  });
  byId('profile-form').addEventListener('submit',event => {
    event.preventDefault();
    const name = byId('display-name').value.trim();
    if (!name) {byId('profile-status').textContent = 'Enter a display name'; return;}
    const select = byId('track-select');
    const track = select.options[select.selectedIndex].text;
    byId('profile-status').textContent = `Profile saved: ${name} · ${track} · updates ${byId('email-updates').checked ? 'on' : 'off'}`;
  });
  byId('load-message').addEventListener('click', event => {
    const button = event.currentTarget;
    button.disabled = true;
    byId('async-result').textContent = 'Loading…';
    setTimeout(() => {byId('async-result').textContent = 'Ready for testing'; button.disabled = false;},700);
  });
  let tasks = [];
  let nextId = 1;
  function drawTasks() {
    const rows = byId('task-rows'); rows.replaceChildren();
    tasks.forEach(task => {
      const row = document.createElement('tr');
      const name = document.createElement('td'); name.textContent = task.name;
      const done = document.createElement('td');
      const checkbox = document.createElement('input'); checkbox.type = 'checkbox'; checkbox.checked = task.done;
      checkbox.setAttribute('aria-label',`Complete ${task.name}`);
      checkbox.addEventListener('change', () => {task.done = checkbox.checked; drawTasks();}); done.appendChild(checkbox);
      const action = document.createElement('td');
      const remove = document.createElement('button'); remove.type = 'button'; remove.textContent = 'Remove';
      remove.setAttribute('aria-label',`Remove ${task.name}`);
      remove.addEventListener('click',() => {tasks = tasks.filter(value => value.id !== task.id); drawTasks();});
      action.appendChild(remove); row.append(name,done,action); rows.appendChild(row);
    });
    byId('task-summary').textContent = `${tasks.filter(task => task.done).length} of ${tasks.length} tasks complete`;
  }
  byId('task-form').addEventListener('submit',event => {
    event.preventDefault();
    const input = byId('task-name'), name = input.value.trim();
    if (!name) {byId('task-validation').textContent = 'Enter a task name.'; return;}
    if (tasks.some(task => task.name === name)) {byId('task-validation').textContent = 'Use a different task name.'; return;}
    tasks.push({id:nextId++,name,done:false}); drawTasks(); input.value = ''; input.focus();
    byId('task-validation').textContent = '';
  });
  byId('confirm-reset').addEventListener('click',() => {
    if (window.confirm('Reset all practice tasks?')) {tasks = [];drawTasks();byId('task-validation').textContent = '';}
  });
  let uploadAttempt = 0;
  byId('sample-file').addEventListener('change',async event => {
    const attempt = ++uploadAttempt;
    const file = event.target.files[0];
    if (!file) {byId('file-result').textContent = 'No file loaded';return;}
    if (file.size > 1000000) {byId('file-result').textContent = 'Choose a text file up to 1 MB';return;}
    try {
      const text = await file.text();
      if (attempt === uploadAttempt) byId('file-result').textContent = `Loaded: ${file.name} · ${text}`;
    } catch (_) {byId('file-result').textContent = 'Could not read the file';}
  });
  byId('download-csv').addEventListener('click',() => {
    const objectUrl = URL.createObjectURL(new Blob(['test,browser,passed,seconds\nlogin,chromium,true,1.2\nsearch,chromium,false,0.8\n'],{type:'text/csv;charset=utf-8'}));
    const link = document.createElement('a');link.href = objectUrl;link.download = 'test-results.csv';
    document.body.appendChild(link);link.click();link.remove();
    setTimeout(() => URL.revokeObjectURL(objectUrl),1000);
  });
  byId('open-window').addEventListener('click',() => window.open('practice-window.html','_blank','noopener'));
})();
