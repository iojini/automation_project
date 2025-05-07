from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.application import Application

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/language_change.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # MOBILE VIEW
    # chrome_options = Options()
    # mobile_emulation = {"deviceName": "Pixel 7"}
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)


    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)

    # firefox_options = FirefoxOptions()
    # firefox_options.add_argument('--headless')
    # service = FirefoxService(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(options=firefox_options, service=service)

    ### BROWSERSTACK ###
    bs_user = 'ireneojini_dAx2pv'
    bs_key = 'MRxqJrbMUgyt6sYB2LxD'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
    #    'os': "OS X",
    #    'osVersion': "Monterey",
    #    'browserName': 'Chrome',
    #    'sessionName': scenario_name,
    #}

    #options = Options()
    #bstack_options = {
    #    'os': "Windows",
    #    'osVersion': "11",
    #    'browserName': 'edge',
    #    'sessionName': scenario_name,
    #}

    #options = FirefoxOptions()
    #bstack_options = {
    #    'os': 'OS X',
    #    'osVersion': 'Ventura',
    #    'browserName': 'Firefox',
    #    'sessionName': scenario_name,
    #}

    options = Options()
    bstack_options = {
        'browserName': 'Chrome',
        'deviceName': 'Google Pixel 7',
        'realMobile': 'true',
        'osVersion': '13.0',
        'sessionName': scenario_name,
     }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    #context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
