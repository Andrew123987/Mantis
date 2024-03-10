import uuid
from selenium.common.exceptions import NoSuchElementException


def test_delete_project(app):
    app.project.move_to_projects_list()
    a = str(uuid.uuid4())
    app.project.project_add(a)
    projects_before = len(app.wd.find_elements_by_class_name('row-1')) + len(app.wd.find_elements_by_class_name('row-2'))

    app.project.move_to_projects_list()
    app.project.delete_project()

    app.project.move_to_projects_list()
    projects_after = len(app.wd.find_elements_by_class_name('row-1')) + len(app.wd.find_elements_by_class_name('row-2'))
    assert projects_before - 1 == projects_after



    #try:
    #    app.project.project_name()
    #    name = app.project.project_name()
    #    project_name = name.text
    #    assert a not in project_name
    #    raise NoSuchElementException("")
    #except NoSuchElementException:
    #    print('0 projects. Test passed')

    app.session.logout()
