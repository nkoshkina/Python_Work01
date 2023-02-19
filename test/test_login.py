def test_login(app):
    app.session.login("admin1","password123")
    assert app.session.is_logged()