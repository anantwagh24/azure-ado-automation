class LoginPage:

    def __init__(self, page):

        self.page = page

    def enter_a_valid_username_in_the_username_field(self):

        self.page.locator(
            "#username"
        ).fill("student")

    def enter_a_valid_password_in_the_password_field(self):

        self.page.locator(
            "#password"
        ).fill("Password123")

    def click_on_the_login_button(self):

        self.page.get_by_role(
            "button",
            name="Submit"
        ).click()