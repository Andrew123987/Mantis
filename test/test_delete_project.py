import time
from random import randrange
from model.project_model import Project


def test_delete_project(app):
    old_list = app.project.get_projects_list()
    index = randrange(len(old_list))
    app.project.delete_by_index(index)
    old_list.remove(old_list[index])
    new_list = app.project.get_projects_list()
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)


def test_delete_project_soap(app, config):
    username, password = config['web_admin']['username'], config['web_admin']['password']
    old_list = app.soap.get_projects_for_user(username=username, password=password)
    app.project.open_manage_projects()
    index = randrange(len(old_list))
    app.project.delete_by_index(index)
    old_list.remove(old_list[index])
    time.sleep(5)
    new_list = app.soap.get_projects_for_user(username=username, password=password)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
