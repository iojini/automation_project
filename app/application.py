from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)