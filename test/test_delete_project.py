import uuid
from selenium.common.exceptions import NoSuchElementException

def test_delete_project(app):
    app.session.login('administrator', 'root')
    app.project.move_to_projects_list()

    a = str(uuid.uuid4())
    app.project.project_add(a)

    app.project.move_to_projects_list()
    app.project.delete_project()

    app.project.move_to_projects_list()
    try:
        app.wd.find_element_by_xpath("//tr[3]/td/a")
        name = app.wd.find_element_by_xpath("//tr[3]/td/a")
        project_name = name.text
        assert a not in project_name
        raise NoSuchElementException("")
    except NoSuchElementException:
        print('0 projects. Test passed')

    app.session.logout()
