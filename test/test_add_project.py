import uuid


def _add_project(app):
    a = str(uuid.uuid4())

    app.project.move_to_projects_list()
    projects_before = len(app.wd.find_elements_by_class_name('row-1')) + len(app.wd.find_elements_by_class_name('row-2'))
    app.project.project_add(a)

    app.project.move_to_projects_list()
    projects_after = len(app.wd.find_elements_by_class_name('row-1')) + len(app.wd.find_elements_by_class_name('row-2'))
    assert projects_before + 1 == projects_after

    #name = app.project.project_name()
    #project_name = name.text
    #assert a in project_name

    app.session.logout()
