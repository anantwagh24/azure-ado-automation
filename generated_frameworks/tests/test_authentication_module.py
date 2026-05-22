from generated_frameworks.utils.playwright_driver import PlaywrightDriver
from generated_frameworks.pages.authentication_module_page import LoginPage

driver = PlaywrightDriver()

driver.navigate("https://practicetestautomation.com/practice-test-login")

page = LoginPage(driver.page)

page.enter_a_valid_username_in_the_username_field()
page.enter_a_valid_password_in_the_password_field()
page.click_on_the_login_button()

driver.wait(5000)
driver.close()
