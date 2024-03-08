import uuid


def test_add_project(app):
    app.session.login('administrator', 'root')
    a = str(uuid.uuid4())
    move_to_projects_list(app)
    project_add(app, a)

    move_to_projects_list(app)
    assert app.wd.find_element_by_xpath("//a[contains(.,a)]")


def move_to_projects_list(app):
    app.wd.find_element_by_link_text('Manage').click()
    app.wd.find_element_by_link_text('Manage Projects').click()


def project_add(app, a):
    app.wd.find_element_by_xpath('//table[3]/tbody/tr/td/form/input[2]').click()
    app.wd.find_element_by_name('name').click()
    app.wd.find_element_by_name('name').send_keys(a)
    app.wd.find_element_by_xpath("//input[@value='Add Project']").click()
