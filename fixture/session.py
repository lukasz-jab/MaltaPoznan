from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self, user, password):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.execute_script("arguments[0].click()", wd.find_element_by_css_selector("div#main-navbar a#btn-header-logIn"))
        wd.execute_script("arguments[0].value='selenium'", wd.find_element_by_css_selector("div.login input[name=username]"))
        wd.execute_script("arguments[0].value='TestSelenium'",
                          wd.find_element_by_css_selector("div.login input[name=password]"))
        wd.execute_script("arguments[0].click()",
                          wd.find_element_by_css_selector("div.login button.btn.btn-primary.btn-raised.hidden-xs"))

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert().accept()
        except NoAlertPresentException as e:
            return False
        return True
