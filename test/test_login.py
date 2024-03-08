def test_login(app):
    logout = app.wd.find_element_by_link_text('Logout')
    if logout.is_displayed():
        logout.click()
    app.session.login('administrator', 'root')
    assert app.session.is_logged_in_as('administrator')
