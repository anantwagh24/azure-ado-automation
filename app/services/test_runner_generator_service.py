class TestRunnerGeneratorService:

    def generate_test_runner(
            self,
            feature_name
    ):

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        content = ""

        content += (
            "from generated_frameworks.utils."
            "playwright_driver "
            "import PlaywrightDriver\n"
        )

        content += (
            f"from generated_frameworks.pages."
            f"{safe_name}_page "
            f"import LoginPage\n\n"
        )

        content += (
            "driver = PlaywrightDriver()\n\n"
        )

        content += (
            "driver.navigate("
            '"https://example.com/login")\n\n'
        )

        content += (
            "page = LoginPage(driver.page)\n\n"
        )

        content += (
            "page.enter_a_valid_username_"
            "in_the_username_field()\n"
        )

        content += (
            "page.enter_a_valid_password_"
            "in_the_password_field()\n"
        )

        content += (
            "page.click_on_the_login_button()\n\n"
        )

        content += (
            "driver.wait(5000)\n"
        )

        content += (
            "driver.close()\n"
        )

        return content