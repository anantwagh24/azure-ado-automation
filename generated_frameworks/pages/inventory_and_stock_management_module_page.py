from app.services.self_healing_service import SelfHealingService

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.self_healing_service = SelfHealingService()

    def safe_fill(
            self,
            primary_locator,
            value,
            fallback_locators
    ):

        for locator in fallback_locators:

            try:

                self.page.locator(locator).fill(value)

                return

            except Exception:

                continue

        page_html = self.page.content()

        repaired_locator = (
            self.self_healing_service
            .repair_locator(
                primary_locator,
                page_html,
                "fill"
            )
        )

        self.page.locator(
            repaired_locator
        ).fill(value)

    def safe_click(
            self,
            primary_locator,
            fallback_locators
    ):

        for locator in fallback_locators:

            try:

                self.page.locator(locator).click()

                return

            except Exception:

                continue

        page_html = self.page.content()

        repaired_locator = (
            self.self_healing_service
            .repair_locator(
                primary_locator,
                page_html,
                "click"
            )
        )

        self.page.locator(
            repaired_locator
        ).click()

    def navigate_to_the_inventory_management_module(self):
        pass

    def select_an_existing_product_from_the_product_list(self):
        pass

    def enter_a_valid_positive_quantity_to_add_to_the_stock(self):
        self.safe_fill(
            "UNKNOWN",
            self.test_data_service.generate_test_data(step),
            ['UNKNOWN']
        )

    def submit_the_stock_addition(self):
        pass

    def attempt_to_add_stock_with_quantity_zero(self):
        pass

    def attempt_to_add_stock_with_a_negative_quantity(self):
        pass

    def submit_the_stock_addition_in_both_cases(self):
        pass

    def attempt_to_add_stock_for_a_product_id_or_name_that_does_not_exist_in_the_system(self):
        pass

    def enter_a_valid_positive_quantity(self):
        self.safe_fill(
            "UNKNOWN",
            self.test_data_service.generate_test_data(step),
            ['UNKNOWN']
        )

    def select_an_existing_product(self):
        pass

    def add_a_valid_positive_quantity_to_the_stock(self):
        pass

    def observe_the_inventory_levels_on_the_dashboard_or_inventory_tracking_screen(self):
        pass

    def navigate_to_the_audit_history_or_stock_adjustment_logs_for_the_product(self):
        pass

    def verify_the_latest_entry_corresponds_to_the_recent_stock_addition(self):
        pass

