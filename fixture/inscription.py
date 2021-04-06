import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from model.inscription import Inscription


class InscriptionHelper():
    def __init__(self, app):
        self.app = app

    def get_inscriptions_all(self):
        wd = self.app.wd
        WebDriverWait(wd, 20).until(lambda d: d.find_elements_by_css_selector(
            "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features']"))
        web_inscriptions = wd.find_elements_by_css_selector(
            "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features']")
        inscriptions = []
        for el in web_inscriptions:
            title = el.find_element_by_css_selector("p.title").text
            id = el.find_element_by_css_selector(
                "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features'] div.feature").get_attribute(
                "id")
            # comments = int(el.find_element_by_css_selector("p.post-data.ng-binding span").text)
            inscriptions.append(Inscription(title=title, id=id))
        return inscriptions

    def comment_inscription(self, inscription, text):
        wd = self.app.wd
        inscription = wd.find_element_by_css_selector(
            "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features'] div[id=" + inscription.id + "]")
        wd.execute_script("arguments[0].click()", inscription)
        wd.find_element_by_css_selector("div.paper div.row.modal-view-row textarea").send_keys(text)
        # if self.app.session.is_element_present(By.CSS_SELECTOR, "div#djDebugToolbar a[title='Hide toolbar']"):
        #     self.app.navigation.hide_panel()
        if self.app.session.is_element_present(By.CSS_SELECTOR, "div[ng-if=isRodoOpen] button"):
            self.app.session.close_rodo()
        submit_button = wd.find_element_by_css_selector("div.paper button#btn-mapModalView-submitComment")
        wd.execute_script("arguments[0].scrollIntoView()", submit_button)
        submit_button.click()
        wd.find_element_by_css_selector("div.paper div.col-md-12.text-right.no-padding button").click()

    def get_comments(self, inscription):
        wd = self.app.wd
        inscription = wd.find_element_by_css_selector(
            "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features'] div[id=" + inscription.id + "]")
        wd.execute_script("arguments[0].click()", inscription)
        web_comments = wd.find_elements_by_css_selector("div#modal-view-comments-content div.col-md-12.comment.paper")
        comments = []
        for comment in web_comments:
            comments.append(comment.text)
        wd.find_element_by_css_selector("div.paper div.col-md-12.text-right.no-padding button").click()
        return comments

    def comments_count(self):
        wd = self.app.wd
        web_comments = wd.find_elements_by_css_selector("div[ui-view=left] div#bottom-left div[ng-repeat='feature in features'] p.post-data.ng-binding span")
        comments_count = []
        for comment in web_comments:
            comments_count.append(int(comment.text))
        return comments_count

    def get_inscriptions_by_category(self):
        wd = self.app.wd
        category_box = WebDriverWait(wd, 10).until(lambda d: d.find_element_by_css_selector("div[ui-view=left] div.col.text-left.ng-scope"))
        category_box.click()
        wd.find_element_by_css_selector("div[ui-view=left] div.col.text-left.ng-scope div.dropdown-cart label").click()
        time.sleep(5)
        WebDriverWait(wd, 10).until(lambda d: d.find_element_by_css_selector("div[ui-view=left] div#bottom-left div[ng-repeat='feature in features']"))
        web_inscriptions = wd.find_elements_by_css_selector(
            "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features']")
        inscriptions = []
        for el in web_inscriptions:
            title = el.find_element_by_css_selector("p.title").text
            id = el.find_element_by_css_selector(
                "div[ui-view=left] div#bottom-left div[ng-repeat='feature in features'] div.feature").get_attribute(
                "id")
            # comments = int(el.find_element_by_css_selector("p.post-data.ng-binding span").text)
            inscriptions.append(Inscription(title=title, id=id))
        return inscriptions
