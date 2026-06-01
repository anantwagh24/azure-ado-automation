import re

from app.services.locator_intelligence_service import (
    LocatorIntelligenceService
)
from app.services.test_data_generator_service import (
    TestDataGeneratorService
)


class PageObjectGeneratorService:

    def __init__(self):

        self.locator_service = (
            LocatorIntelligenceService()
        )
        self.test_data_service = (
            TestDataGeneratorService()
        )

    def sanitize_name(
            self,
            text
    ):

        text = text.lower()

        text = re.sub(
            r'[^a-zA-Z0-9 ]',
            '',
            text
        )

        return (
            text
            .replace(" ", "_")
        )

    def generate_page_objects(
            self,
            test_cases
    ):

        page_object_content = (
            "from app.services."
            "self_healing_service "
            "import SelfHealingService\n\n"
        )

        page_object_content += (
            "class LoginPage:\n\n"
        )

        # Constructor
        page_object_content += (
            "    def __init__(self, page):\n"
        )

        page_object_content += (
            "        self.page = page\n"
        )

        page_object_content += (
            "        self.self_healing_service = "
            "SelfHealingService()\n\n"
        )

        # Self-Healing Fill
        page_object_content += (
            "    def safe_fill(\n"
        )

        page_object_content += (
            "            self,\n"
        )

        page_object_content += (
            "            primary_locator,\n"
        )

        page_object_content += (
            "            value,\n"
        )

        page_object_content += (
            "            fallback_locators\n"
        )

        page_object_content += (
            "    ):\n\n"
        )

        page_object_content += (
            "        for locator in "
            "fallback_locators:\n\n"
        )

        page_object_content += (
            "            try:\n\n"
        )

        page_object_content += (
            "                self.page.locator("
            "locator).fill(value)\n\n"
        )

        page_object_content += (
            "                return\n\n"
        )

        page_object_content += (
            "            except Exception:\n\n"
        )

        page_object_content += (
            "                continue\n\n"
        )

        # AI Self-Healing
        page_object_content += (
            "        page_html = "
            "self.page.content()\n\n"
        )

        page_object_content += (
            "        repaired_locator = (\n"
        )

        page_object_content += (
            "            self.self_healing_service\n"
        )

        page_object_content += (
            "            .repair_locator(\n"
        )

        page_object_content += (
            "                primary_locator,\n"
        )

        page_object_content += (
            "                page_html,\n"
        )

        page_object_content += (
            '                "fill"\n'
        )

        page_object_content += (
            "            )\n"
        )

        page_object_content += (
            "        )\n\n"
        )

        page_object_content += (
            "        self.page.locator(\n"
        )

        page_object_content += (
            "            repaired_locator\n"
        )

        page_object_content += (
            "        ).fill(value)\n\n"
        )

        # Self-Healing Click
        page_object_content += (
            "    def safe_click(\n"
        )

        page_object_content += (
            "            self,\n"
        )

        page_object_content += (
            "            primary_locator,\n"
        )

        page_object_content += (
            "            fallback_locators\n"
        )

        page_object_content += (
            "    ):\n\n"
        )

        page_object_content += (
            "        for locator in "
            "fallback_locators:\n\n"
        )

        page_object_content += (
            "            try:\n\n"
        )

        page_object_content += (
            "                self.page.locator("
            "locator).click()\n\n"
        )

        page_object_content += (
            "                return\n\n"
        )

        page_object_content += (
            "            except Exception:\n\n"
        )

        page_object_content += (
            "                continue\n\n"
        )

        # AI Self-Healing
        page_object_content += (
            "        page_html = "
            "self.page.content()\n\n"
        )

        page_object_content += (
            "        repaired_locator = (\n"
        )

        page_object_content += (
            "            self.self_healing_service\n"
        )

        page_object_content += (
            "            .repair_locator(\n"
        )

        page_object_content += (
            "                primary_locator,\n"
        )

        page_object_content += (
            "                page_html,\n"
        )

        page_object_content += (
            '                "click"\n'
        )

        page_object_content += (
            "            )\n"
        )

        page_object_content += (
            "        )\n\n"
        )

        page_object_content += (
            "        self.page.locator(\n"
        )

        page_object_content += (
            "            repaired_locator\n"
        )

        page_object_content += (
            "        ).click()\n\n"
        )

        generated_methods = []

        for test_case in test_cases:

            steps = test_case.get(
                "steps",
                []
            )

            for step in steps:

                method_name = (
                    self.sanitize_name(step)
                )

                if (
                        method_name
                        not in generated_methods
                ):

                    generated_methods.append(
                        method_name
                    )

                    locators = (
                        self.locator_service
                        .generate_locator(step)
                    )

                    primary_locator = (
                        locators[0]
                    )

                    page_object_content += (
                        f"    def "
                        f"{method_name}(self):\n"
                    )

                    # Fill Actions
                    if (
                            "enter"
                            in step.lower()
                    ):

                        page_object_content += (
                            f"        self.safe_fill(\n"
                        )

                        page_object_content += (
                            f'            "{primary_locator}",\n'
                        )

                        page_object_content += (
                            f'            self.test_data_service.generate_test_data(step),\n'
                        )

                        page_object_content += (
                            f"            {locators}\n"
                        )

                        page_object_content += (
                            f"        )\n\n"
                        )

                    # Click Actions
                    elif (
                            "click"
                            in step.lower()
                    ):

                        page_object_content += (
                            f"        self.safe_click(\n"
                        )

                        page_object_content += (
                            f'            "{primary_locator}",\n'
                        )

                        page_object_content += (
                            f"            {locators}\n"
                        )

                        page_object_content += (
                            f"        )\n\n"
                        )

                    else:

                        page_object_content += (
                            "        pass\n\n"
                        )

        return page_object_content