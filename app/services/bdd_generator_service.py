class BDDGeneratorService:

    def generate_feature_file_content(
            self,
            feature_name,
            test_cases
    ):

        feature_content = f"Feature: {feature_name}\n\n"

        for test_case in test_cases:

            feature_content += (
                f"Scenario: {test_case['title']}\n"
            )

            steps = test_case.get("steps", [])

            if len(steps) > 0:

                feature_content += (
                    f"  Given {steps[0]}\n"
                )

            for step in steps[1:-1]:

                feature_content += (
                    f"  And {step}\n"
                )

            if len(steps) > 1:

                feature_content += (
                    f"  When {steps[-1]}\n"
                )

            feature_content += (
                f"  Then "
                f"{test_case['expected_result']}\n\n"
            )

        return feature_content