from playwright.sync_api import expect

from generated_frameworks.utils.playwright_driver import PlaywrightDriver

from generated_frameworks.pages.authentication_module_page import LoginPage

from app.services.reporting_service import (
    ReportingService
)


driver = PlaywrightDriver()

report_service = ReportingService()

driver.navigate(
    "https://practicetestautomation.com/practice-test-login"
)

page = LoginPage(driver.page)

page.enter_a_valid_username_in_the_username_field()

page.enter_a_valid_password_in_the_password_field()

page.click_on_the_login_button()


# AI Assertion

expect(
    driver.page.locator(
        ".post-title"
    )
).to_be_visible()


# Reporting Dashboard

report_service.generate_report(
    {
        "test_name":
            "Authentication Test",

        "status":
            "PASS"
    }
)

driver.wait(5000)

driver.close()