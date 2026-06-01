class AssertionGeneratorService:

    def generate_assertion(
            self,
            expected_result
    ):

        expected_result = (
            expected_result.lower()
        )

        if "dashboard" in expected_result:

            return """

expect(
    page.locator("text=Dashboard")
).to_be_visible()

"""

        elif "error" in expected_result:

            return """

expect(
    page.locator(".error-message")
).to_be_visible()

"""

        return """
# Assertion Placeholder
"""