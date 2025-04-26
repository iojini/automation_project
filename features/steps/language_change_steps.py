from behave import given, when, then


@given("user navigates to the login page")
def navigate_to_main(context):
    context.app.login_page.open()


@given("user logs in with email and password")
def login_with_credentials(context):
    email = "*****"
    password = "*****"
    context.app.login_page.login(email, password)


@given("user clicks on the settings icon")
def click_settings_icon(context):
    context.app.main_page.click_settings_icon()
    context.driver.save_screenshot("before_language_change.png")


@when("user clicks on language icon")
def select_russian_language(context):
    context.app.settings_page.open_language_menu()


@when("user selects the Russian language option")
def select_russian_language(context):
    context.app.settings_page.select_russian_language()


@then("the current language selected should be Russian")
def verify_language_selection(context):
    context.app.settings_page.verify_language_changed_to_russian()
    context.driver.save_screenshot("after_language_change.png")
