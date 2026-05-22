import os


class FrameworkStorage:

    OUTPUT_DIR = "generated_frameworks/features"

    @classmethod
    def save_feature_file(
            cls,
            feature_name,
            content
    ):

        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"{cls.OUTPUT_DIR}/{safe_name}.feature"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path

    @classmethod
    def save_step_definition_file(
            cls,
            feature_name,
            content
    ):

        output_dir = (
            "generated_frameworks/"
            "step_definitions"
        )

        os.makedirs(output_dir, exist_ok=True)

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"{output_dir}/"
            f"{safe_name}_steps.py"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path

    @classmethod
    def save_business_flow_file(
            cls,
            feature_name,
            content
    ):

        output_dir = (
            "generated_frameworks/"
            "business_flows"
        )

        os.makedirs(output_dir, exist_ok=True)

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"{output_dir}/"
            f"{safe_name}_flows.py"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path

    @classmethod
    def save_page_object_file(
            cls,
            feature_name,
            content
    ):

        output_dir = (
            "generated_frameworks/pages"
        )

        os.makedirs(output_dir, exist_ok=True)

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"{output_dir}/"
            f"{safe_name}_page.py"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path

    @classmethod
    def save_playwright_driver(
            cls,
            content
    ):

        output_dir = (
            "generated_frameworks/utils"
        )

        os.makedirs(output_dir, exist_ok=True)

        file_path = (
            f"{output_dir}/"
            f"playwright_driver.py"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path

    @classmethod
    def save_test_runner(
            cls,
            feature_name,
            content
    ):

        output_dir = (
            "generated_frameworks/tests"
        )

        os.makedirs(output_dir, exist_ok=True)

        safe_name = (
            feature_name
            .replace(" ", "_")
            .lower()
        )

        file_path = (
            f"{output_dir}/"
            f"test_{safe_name}.py"
        )

        with open(file_path, "w") as file:

            file.write(content)

        return file_path