from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SETTINGS_ICON = (By.CSS_SELECTOR, 'a.settings-link.w-inline-block')

    def click_settings_icon(self):
        self.wait_until_clickable_click(*self.SETTINGS_ICON)