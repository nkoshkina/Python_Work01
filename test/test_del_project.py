# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.project import Project
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(projectName="test project", status="obsolete", igs='1', viewStatus="public", description="Descr"))
    old_projects = db.get_projects_list_db()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_projectS_list_db()
    old_projects.remove(project)
    assert new_projects == old_projects





