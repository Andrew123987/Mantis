import time
from datetime import datetime
from model.project_model import Project

proj_name_raw = datetime.now()


def test_add_new_project(app):
    app.project.move_to_manage_projects()
    old_list = app.project.move_to_projects_list()
    proj_name = ("test " + str(proj_name_raw))[:-7]
    app.project.add_new_project(Project(name=proj_name))
    old_list.append(Project(name=proj_name))
    new_list = app.project.move_to_projects_list()
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()


def test_add_new_project_soap(app, config):
    app.project.move_to_projects_list()
    old_list = app.soap.get_projects_for_user(username=config['web_admin']['username'],
                                              password=config['web_admin']['password'])
    project_name = ("test " + str(proj_name_raw))[:-7]
    app.project.add_new_project(Project(name=project_name))
    time.sleep(5)
    old_list.append(Project(name=project_name))
    new_list = app.soap.get_projects_for_user(username=config['web_admin']['username'],
                                              password=config['web_admin']['password'])
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()
