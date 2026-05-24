from generated_frameworks.utils.playwright_driver import PlaywrightDriver

from generated_frameworks.pages.invoice_module_page import LoginPage


driver = PlaywrightDriver()

page = driver.get_page()

page.goto(
    "https://practicetestautomation.com/practice-test-login/"
)

login_page = LoginPage(page)

login_page.enter_a_valid_username_in_the_username_field()

login_page.enter_a_valid_password_in_the_password_field()

login_page.click_on_the_login_button()

input(
    "Press Enter to close browser..."
)

driver.close()