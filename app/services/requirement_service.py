from app.connectors.azure_devops_connector import AzureDevOpsConnector
from app.services.ai_service import AIService
from app.utils.file_storage import FileStorage
from app.services.bdd_generator_service import BDDGeneratorService
from app.utils.framework_storage import FrameworkStorage
from app.services.step_definition_generator_service import ( StepDefinitionGeneratorService)
from app.services.business_flow_generator_service import (    BusinessFlowGeneratorService)
from app.services.page_object_generator_service import (    PageObjectGeneratorService)
from app.services.playwright_generator_service import (    PlaywrightGeneratorService)
from app.services.test_runner_generator_service import ( TestRunnerGeneratorService )
from app.services.ado_test_case_service import (    ADOTestCaseService)

class RequirementService:

    def __init__(self):
        self.connector = AzureDevOpsConnector()
        self.ai_service = AIService()
        self.bdd_service = BDDGeneratorService()
        self.step_definition_service = (
            StepDefinitionGeneratorService()
        )
        self.business_flow_service = (
            BusinessFlowGeneratorService()
        )
        self.page_object_service = (
            PageObjectGeneratorService()
        )
        self.playwright_service = (
            PlaywrightGeneratorService()
        )
        self.test_runner_service = (
            TestRunnerGeneratorService()
        )
        self.ado_test_case_service = (
            ADOTestCaseService()
        )

    def fetch_requirement(self, work_item_id):

        data = self.connector.fetch_complete_hierarchy(work_item_id)

        return data

    def generate_test_cases(self, work_item_id):
        requirement_data = self.connector.fetch_complete_hierarchy(work_item_id)

        test_cases = self.ai_service.generate_test_cases(requirement_data)

        file_path = FileStorage.save_test_cases(
            work_item_id,
            test_cases
        )

        return {
            "message": "Test cases generated successfully",
            "file_path": file_path,
            "test_cases": test_cases
        }

    def generate_bdd_feature_file(
            self,
            work_item_id
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(work_item_id)
        )

        test_cases = (
            self.ai_service
            .generate_test_cases(requirement_data)
        )

        feature_content = (
            self.bdd_service
            .generate_feature_file_content(
                requirement_data["title"],
                test_cases
            )
        )

        file_path = (
            FrameworkStorage
            .save_feature_file(
                requirement_data["title"],
                feature_content
            )
        )

        return {
            "message": "BDD feature file generated successfully",
            "file_path": file_path,
            "feature_content": feature_content
        }

    def generate_step_definitions(
            self,
            work_item_id
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(work_item_id)
        )

        test_cases = (
            self.ai_service
            .generate_test_cases(requirement_data)
        )

        feature_content = (
            self.bdd_service
            .generate_feature_file_content(
                requirement_data["title"],
                test_cases
            )
        )

        step_definitions = (
            self.step_definition_service
            .generate_step_definitions(
                feature_content
            )
        )

        file_path = (
            FrameworkStorage
            .save_step_definition_file(
                requirement_data["title"],
                step_definitions
            )
        )

        return {
            "message":
                "Step definitions generated successfully",

            "file_path": file_path,

            "step_definitions": step_definitions
        }

    def generate_business_flows(
            self,
            work_item_id
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(work_item_id)
        )

        test_cases = (
            self.ai_service
            .generate_test_cases(requirement_data)
        )

        business_flows = (
            self.business_flow_service
            .generate_business_flows(
                test_cases
            )
        )

        file_path = (
            FrameworkStorage
            .save_business_flow_file(
                requirement_data["title"],
                business_flows
            )
        )

        return {
            "message":
                "Business flows generated successfully",

            "file_path": file_path,

            "business_flows": business_flows
        }

    def generate_page_objects(
            self,
            work_item_id
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(work_item_id)
        )

        test_cases = (
            self.ai_service
            .generate_test_cases(requirement_data)
        )

        page_objects = (
            self.page_object_service
            .generate_page_objects(
                test_cases
            )
        )

        file_path = (
            FrameworkStorage
            .save_page_object_file(
                requirement_data["title"],
                page_objects
            )
        )

        return {
            "message":
                "Page objects generated successfully",

            "file_path": file_path,

            "page_objects": page_objects
        }

    def generate_playwright_framework(self):
        playwright_content = (
            self.playwright_service
            .generate_playwright_base()
        )

        file_path = (
            FrameworkStorage
            .save_playwright_driver(
                playwright_content
            )
        )

        return {
            "message":
                "Playwright framework generated successfully",

            "file_path": file_path,

            "content": playwright_content
        }

    def generate_test_runner(
            self,
            work_item_id
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(work_item_id)
        )

        test_runner = (
            self.test_runner_service
            .generate_test_runner(
                requirement_data["title"]
            )
        )

        file_path = (
            FrameworkStorage
            .save_test_runner(
                requirement_data["title"],
                test_runner
            )
        )

        return {
            "message":
                "Executable test runner generated",

            "file_path": file_path,

            "content": test_runner
        }

    def push_test_cases_to_ado(
            self,
            work_item_id,
            target
    ):
        requirement_data = (
            self.connector
            .fetch_complete_hierarchy(
                work_item_id
            )
        )

        test_cases = (
            self.ai_service
            .generate_test_cases(
                requirement_data
            )
        )

        created_test_cases = (
            self.ado_test_case_service
            .push_test_cases(
                test_cases,
                requirement_data,
                target
            )
        )

        return {
            "message":
                "Test cases pushed to ADO successfully",

            "created_test_cases":
                created_test_cases
        }

    def generate_playwright_tests(
            self,
            work_item_id
    ):
        import os

        test_file_content = """
    from generated_frameworks.utils.playwright_driver import PlaywrightDriver

    from generated_frameworks.pages.finance_module_page import LoginPage


    driver = PlaywrightDriver()

    page = driver.get_page()

    page.goto(
        "https://practicetestautomation.com/practice-test-login/"
    )

    login_page = LoginPage(page)

    login_page.enter_a_valid_username_in_the_username_field()

    login_page.enter_a_valid_password_in_the_password_field()

    login_page.click_on_the_login_button()

    input(
        "Press Enter to close browser..."
    )

    driver.close()
    """

        os.makedirs(
            "generated_frameworks/tests",
            exist_ok=True
        )

        file_path = (
            "generated_frameworks/tests/"
            "test_finance_module.py"
        )

        with open(
                file_path,
                "w"
        ) as file:
            file.write(
                test_file_content
            )

        return {

            "message":
                "Playwright tests generated successfully",

            "file_path":
                file_path

        }