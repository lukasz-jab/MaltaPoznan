import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


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

    def open_legend_panel(self):
        wd = self.app.wd
        legend_button = WebDriverWait(wd, 10).until(lambda d: d.find_element_by_css_selector(
            "div.ol-unselectable.ol-control.layer-switcher.shown button[title='Legend']"))
        legend_button.click()
        wd.find_element_by_css_selector(
            "div.ol-unselectable.ol-control.layer-switcher.shown div.panel label[for='Open-Street Map_1']").click()
        wd.find_element_by_css_selector(
            "div.ol-unselectable.ol-control.layer-switcher.shown div.panel label[for='Województwa_100']").click()

    def add_entry(self, title):
        wd = self.app.wd
        self.entry_set_title(title)
        self.entry_set_image()
        self.entry_draw_map()
        self.close_entry()

    def entry_draw_map(self):
        wd = self.app.wd
        map = wd.find_element_by_css_selector("div#right-side-map")
        action = ActionChains(wd)
        action.move_to_element_with_offset(map, 100, 100)
        action.click()
        action.click()
        action.click()
        action.click()
        action.perform()
        wd.find_element_by_css_selector(
            "div.col-xs-12.col-md-6.text-right.align-right-bottom button#btn-mapModalAdd-send").click()

    def entry_set_image(self):
        wd = self.app.wd
        image = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources/ok.jpeg")
        wd.find_element_by_css_selector("div.form-inline.visible-lg button").send_keys("")
        wd.find_element_by_css_selector("div.form-inline.visible-lg button").send_keys(image)
        wd.find_element_by_css_selector("button#btn-mapModalAdd-draw-Polygon").click()

    def entry_set_title(self, title):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#left-side a#btn-leftSide-addThread").click()
        wd.find_element_by_css_selector("div.m-modals.ng-scope input#input-opened-textField-1").send_keys(title)
        wd.find_element_by_css_selector("label.btn.btn-primary.ng-binding.ng-scope").click()

    def close_entry(self):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(lambda d: d.find_element_by_css_selector("div.paper div.col-md-12.text-right.no-padding button"))
        wd.find_element_by_css_selector("div.paper div.col-md-12.text-right.no-padding button").click()

    def hide_panel(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#djDebugToolbar a[title='Hide toolbar']").click()
