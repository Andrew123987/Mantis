def _login(app, config):
    assert app.session.is_logged_in_as('administrator')
    app.session.logout()

