import uuid


def test_add_project(app):
    app.session.login('administrator', 'root')

    a = str(uuid.uuid4())

    app.project.move_to_projects_list()
    app.project.project_add(a)

    app.project.move_to_projects_list()
    name = app.wd.find_element_by_xpath("//tr[3]/td/a")
    project_name = name.text
    assert a in project_name

    app.session.logout()
