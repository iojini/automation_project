from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.find_element(*locator).click()

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_until_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator))