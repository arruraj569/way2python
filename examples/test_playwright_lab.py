"""Run with --base-url http://localhost:8080/way2python."""
from playwright.sync_api import expect

def test_login_and_rejection(page, base_url):
    page.goto(f'{base_url}/practice.html')
    page.get_by_label('Email',exact=True).fill('learner@example.test')
    page.get_by_label('Password',exact=True).fill('wrong')
    page.get_by_role('button',name='Sign in',exact=True).click()
    expect(page.get_by_test_id('login-status')).to_have_text('Invalid credentials')
    page.get_by_label('Password',exact=True).fill('python123')
    page.get_by_role('button',name='Sign in',exact=True).click()
    expect(page.get_by_test_id('login-status')).to_have_text('Welcome, learner!')

def test_profile_and_wait(page, base_url):
    page.goto(f'{base_url}/practice.html')
    page.get_by_label('Display name').fill('Mira')
    page.get_by_label('Learning track').select_option('api')
    page.get_by_label('Email updates').check()
    page.get_by_role('button',name='Save profile',exact=True).click()
    expect(page.get_by_test_id('profile-status')).to_have_text('Profile saved: Mira · API testing · updates on')
    page.get_by_role('button',name='Load message',exact=True).click()
    expect(page.get_by_test_id('async-result')).to_have_text('Ready for testing')

def test_task_table_and_dialog(page, base_url):
    page.goto(f'{base_url}/practice.html')
    page.get_by_label('Task name').fill('API smoke checks')
    page.get_by_role('button',name='Add task',exact=True).click()
    row=page.get_by_role('row').filter(has_text='API smoke checks')
    row.get_by_role('checkbox').check()
    expect(page.get_by_test_id('task-summary')).to_have_text('1 of 1 tasks complete')
    page.once('dialog',lambda dialog:dialog.dismiss())
    page.get_by_role('button',name='Reset tasks',exact=True).click()
    expect(row).to_be_visible()
    page.once('dialog',lambda dialog:dialog.accept())
    page.get_by_role('button',name='Reset tasks',exact=True).click()
    expect(page.get_by_test_id('task-summary')).to_have_text('0 of 0 tasks complete')

def test_frame_upload_download_and_popup(page, base_url, tmp_path):
    page.goto(f'{base_url}/practice.html')
    frame=page.frame_locator('#practice-frame')
    frame.get_by_label('Frame email').fill('mira@example.test')
    frame.get_by_role('button',name='Save email',exact=True).click()
    expect(frame.get_by_role('status')).to_have_text('Saved: mira@example.test')
    page.get_by_label('Upload a text file').set_input_files({'name':'sample.txt','mimeType':'text/plain','buffer':b'automation notes'})
    expect(page.get_by_test_id('file-result')).to_have_text('Loaded: sample.txt · automation notes')
    with page.expect_download() as result:
        page.get_by_role('button',name='Download sample CSV',exact=True).click()
    destination=tmp_path/'results.csv'
    result.value.save_as(destination)
    assert 'search,chromium,false,0.8' in destination.read_text()
    with page.expect_popup() as popup:
        page.get_by_role('button',name='Open practice window',exact=True).click()
    expect(popup.value.get_by_role('heading',name='Practice window',exact=True)).to_be_visible()
    popup.value.close()
