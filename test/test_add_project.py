# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project(app, db, json_projects):
    project0 = json_projects
    old_projects = db.get_projects_list_db()
    app.project.create(project0)
    new_projects = db.get_projects_list_db()
    old_projects.append(project0)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


