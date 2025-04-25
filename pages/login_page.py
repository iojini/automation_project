from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def login(self, email, password):
        self.wait_until_visible(*self.EMAIL)
        self.input_text(email, *self.EMAIL)
        self.input_text(password, *self.PASSWORD)
        self.wait_until_clickable_click(*self.CONTINUE_BTN)