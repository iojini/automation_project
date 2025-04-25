from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class SettingsPage(Page):
    LANGUAGE_BUTTON = (By.ID, "w-dropdown-toggle-0")
    RUSSIAN_OPTION = (By.XPATH, "//a[@lang='ru']")


    def open_language_menu(self):
        self.wait_until_visible(*self.LANGUAGE_BUTTON)
        #lang_button = self.find_element(*self.LANGUAGE_BUTTON)
        ActionChains(self.driver).move_to_element(self.find_element(*self.LANGUAGE_BUTTON)).perform()
        self.wait_until_visible(*self.RUSSIAN_OPTION)

    def select_russian_language(self):
        #self.wait_until_visible(*self.RUSSIAN_OPTION)
        self.wait_until_clickable_click(*self.RUSSIAN_OPTION)

    def verify_language_changed_to_russian(self):
        text = self.find_element(*self.LANGUAGE_BUTTON).text.strip()
        assert text == "RU", f"Expected language to be RU, but got '{text}'"


