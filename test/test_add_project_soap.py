# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project_soap(app, db, json_projects):
    project0 = json_projects
    old_projects = app.soap.get_projects_list_soap()
    app.project.create(project0)
    new_projects = app.soap.get_projects_list_soap()
    old_projects.append(project0)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


