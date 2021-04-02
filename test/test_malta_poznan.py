

def test_malta_poznan(app, user):
    app.navigation.open_home()
    app.session.login(user['user'], user['password'])
    app.navigation.hide_devel_panel()
    app.navigation.add_entry()