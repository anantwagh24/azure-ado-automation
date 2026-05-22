import re


class StepDefinitionGeneratorService:

    def sanitize_function_name(
            self,
            step
    ):

        step = step.lower()

        step = re.sub(
            r'[^a-zA-Z0-9 ]',
            '',
            step
        )

        return (
            step
            .replace(" ", "_")
        )

    def generate_step_definitions(
            self,
            feature_content
    ):

        lines = feature_content.splitlines()

        generated_steps = []

        step_definitions = (
            "from behave import given, when, then\n\n"
        )

        for line in lines:

            line = line.strip()

            if (
                line.startswith("Given")
                or line.startswith("When")
                or line.startswith("Then")
                or line.startswith("And")
            ):

                step_text = (
                    line
                    .replace("Given ", "")
                    .replace("When ", "")
                    .replace("Then ", "")
                    .replace("And ", "")
                )

                if step_text not in generated_steps:

                    generated_steps.append(step_text)

                    function_name = (
                        self.sanitize_function_name(
                            step_text
                        )
                    )

                    decorator = "given"

                    if line.startswith("When"):
                        decorator = "when"

                    elif line.startswith("Then"):
                        decorator = "then"

                    step_definitions += (
                        f"@{decorator}"
                        f"(\"{step_text}\")\n"
                    )

                    step_definitions += (
                        f"def "
                        f"{function_name}(context):\n"
                    )

                    step_definitions += (
                        f"    pass\n\n"
                    )

        return step_definitions