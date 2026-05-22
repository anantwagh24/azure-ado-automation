class PlaywrightGeneratorService:

    def generate_playwright_base(self):

        content = ""

        content += (
            "from playwright.sync_api "
            "import sync_playwright\n\n"
        )

        content += (
            "class PlaywrightDriver:\n\n"
        )

        content += (
            "    def __init__(self):\n"
        )

        content += (
            "        self.playwright = "
            "sync_playwright().start()\n"
        )

        content += (
            "        self.browser = "
            "self.playwright.chromium.launch("
            "headless=False)\n"
        )

        content += (
            "        self.page = "
            "self.browser.new_page()\n\n"
        )

        content += (
            "    def navigate(self, url):\n"
        )

        content += (
            "        self.page.goto(url)\n\n"
        )

        content += (
            "    def click(self, locator):\n"
        )

        content += (
            "        self.page.locator(locator)"
            ".click()\n\n"
        )

        content += (
            "    def fill(self, locator, value):\n"
        )

        content += (
            "        self.page.locator(locator)"
            ".fill(value)\n\n"
        )

        content += (
            "    def get_text(self, locator):\n"
        )

        content += (
            "        return self.page"
            ".locator(locator)"
            ".inner_text()\n\n"
        )

        content += (
            "    def wait(self, milliseconds):\n"
        )

        content += (
            "        self.page.wait_for_timeout("
            "milliseconds)\n\n"
        )

        content += (
            "    def close(self):\n"
        )

        content += (
            "        self.browser.close()\n"
        )

        return content