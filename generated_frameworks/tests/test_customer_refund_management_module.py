

from playwright.sync_api import expect

from generated_frameworks.utils.playwright_driver import PlaywrightDriver

from generated_frameworks.pages.customer_refund_management_module_page import LoginPage

from app.services.reporting_service import (
    ReportingService
)


driver = PlaywrightDriver()

report_service = ReportingService()

page = driver.get_page()

page.goto(
    "https://practicetestautomation.com/practice-test-login/"
)

login_page = LoginPage(page)


# Dynamic Test Execution

login_page.enter_a_valid_username_in_the_username_field()

login_page.enter_a_valid_password_in_the_password_field()

login_page.click_on_the_login_button()


# AI Assertion Generation

expect(
    page.locator(
        ".post-title"
    )
).to_be_visible()


# AI Reporting Dashboard

report_service.generate_report(
    {
        "epic_name":
            "customer_refund_management_module",

        "test_name":
            "AI Generated Test",

        "status":
            "PASS"
    }
)


input(
    "Press Enter to close browser..."
)

driver.close()

