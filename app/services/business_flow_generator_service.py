import re


class BusinessFlowGeneratorService:

    def sanitize_function_name(
            self,
            title
    ):

        title = title.lower()

        title = re.sub(
            r'[^a-zA-Z0-9 ]',
            '',
            title
        )

        return (
            title
            .replace(" ", "_")
        )

    def generate_business_flows(
            self,
            test_cases
    ):

        business_flows = (
            "class BusinessFlows:\n\n"
        )

        for test_case in test_cases:

            function_name = (
                self.sanitize_function_name(
                    test_case["title"]
                )
            )

            business_flows += (
                f"    def "
                f"{function_name}(self):\n"
            )

            steps = test_case.get("steps", [])

            for step in steps:

                business_flows += (
                    f"        # {step}\n"
                )

            business_flows += (
                f"        pass\n\n"
            )

        return business_flows