import os
import time


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        base_url = self.app.base_url
        wd.get(base_url)

    def hide_devel_panel(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#djDebugToolbar a[title='Hide toolbar']").click()
        wd.find_element_by_css_selector("div.ol-unselectable.ol-control.layer-switcher.shown button[title='Legend']").click()
        wd.find_element_by_css_selector("div.ol-unselectable.ol-control.layer-switcher.shown div.panel label[for='Open-Street Map_1']").click()
        wd.find_element_by_css_selector(
            "div.ol-unselectable.ol-control.layer-switcher.shown div.panel label[for='Województwa_100']").click()

    def add_entry(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#left-side a#btn-leftSide-addThread").click()
        wd.find_element_by_css_selector("div.m-modals.ng-scope input#input-opened-textField-1").send_keys("Tytuł" + str(int(time.time() * 1000)))
