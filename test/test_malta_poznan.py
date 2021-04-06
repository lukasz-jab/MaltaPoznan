import time


def test_malta_poznan(app, user):
    app.navigation.open_home()
    app.session.login(user['user'], user['password'])
    app.navigation.hide_devel_panel()
    app.navigation.open_legend_panel()
    old_inscriptions = app.inscription.get_inscriptions_all()
    app.navigation.add_entry("Tytuł" + str(int(time.time() * 1000)))
    malta_list = list(filter(lambda x: x.title == "Malta Poznań", old_inscriptions))
    malta = malta_list[0]
    app.inscription.comment_inscription(malta, "Komentarz do Malta")
    app.wd.refresh()
    first_window_malta_comments = app.inscription.get_comments(malta)
    first_window_inscriptions = app.inscription.get_inscriptions_by_category()
    first_window_comments_sum = app.inscription.comments_count()

    first_window = app.wd.window_handles[0]
    app.wd.execute_script("window.open()")
    second_window = app.wd.window_handles[1]
    app.wd.switch_to.window(second_window)
    app.navigation.open_home()

    new_inscriptions = app.inscription.get_inscriptions_by_category()
    assert len(first_window_inscriptions) == len(new_inscriptions)

    new_malta_comments = app.inscription.get_comments(malta)
    assert first_window_malta_comments == new_malta_comments

    new_window_comments_count = app.inscription.comments_count()
    assert sum(first_window_comments_sum) == sum(new_window_comments_count)