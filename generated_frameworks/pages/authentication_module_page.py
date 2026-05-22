class LoginPage:

    def __init__(self, page):
        self.page = page

    def leave_the_username_field_empty(self):
        pass

    def enter_a_valid_password_in_the_password_field(self):
        self.page.locator("#password").fill("Password123")

    def enter_a_valid_username_in_the_username_field(self):
        self.page.locator("#username").fill("student")

    def click_on_the_login_button(self):
        self.page.get_by_role("button", name="Submit").click()

    def leave_the_password_field_empty(self):
        pass

    def enter_an_invalid_username_in_the_username_field(self):
        self.page.locator("#username").fill("test_data")

    def enter_an_invalid_password_in_the_password_field(self):
        self.page.locator("#password").fill("test_data")

    def check_for_session_creation_in_the_browser_or_server(self):
        pass

    def leave_both_username_and_password_fields_empty(self):
        pass

