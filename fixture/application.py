from selenium import webdriver

from fixture.inscription import InscriptionHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url, user, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.maximize_window()
        self.base_url = base_url
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.inscription = InscriptionHelper(self)

    def destroy(self):
        self.wd.quit()
