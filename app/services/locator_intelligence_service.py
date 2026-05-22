class LocatorIntelligenceService:

    def generate_locator(self, step):

        step = step.lower()

        # Username
        if "username" in step:

            return [
                '#username',
                'input[name="username"]',
                'input[placeholder="Username"]'
            ]

        # Password
        elif "password" in step:

            return [
                '#password',
                'input[name="password"]',
                'input[placeholder="Password"]'
            ]

        # Login Button
        elif (
            "login button" in step
            or "click login" in step
        ):

            return [
                'button:has-text("Login")',
                'input[type="submit"]'
            ]

        return ['UNKNOWN']