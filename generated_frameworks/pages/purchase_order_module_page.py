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

    def navigate_to_the_purchase_order_creation_page(self):
        pass

    def attempt_to_submit_the_purchase_order_form_without_filling_any_fields(self):
        pass

    def attempt_to_submit_the_form_by_filling_only_some_mandatory_fields_leaving_others_blank(self):
        pass

    def observe_validation_messages_for_each_mandatory_field_left_blank(self):
        pass

    def enter_invalid_data_formats_in_fields_such_as_date_quantity_price_etc(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

    def attempt_to_submit_the_purchase_order_form(self):
        pass

    def observe_system_behavior_and_validation_messages(self):
        pass

    def submit_the_purchase_order_form_with_valid_data(self):
        pass

    def observe_the_system_response_after_submission(self):
        pass

    def complete_the_purchase_order_form_with_valid_data(self):
        pass

    def submit_the_purchase_order_for_approval(self):
        pass

    def verify_that_the_purchase_order_status_changes_to_pending_approval_or_equivalent(self):
        pass

    def attempt_to_submit_the_purchase_order_without_obtaining_the_required_approvals(self):
        pass

    def observe_system_behavior_and_any_error_or_warning_messages(self):
        pass

    def enter_valid_data_into_all_required_fields_such_as_vendor_name_item_details_quantity_price_delivery_date_etc(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

    def verify_that_the_data_entered_is_accepted_without_errors(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

    def from_the_main_dashboard_or_menu_select_the_option_to_create_a_new_purchase_order(self):
        pass

    def verify_that_the_purchase_order_creation_page_loads_successfully(self):
        pass

    def submit_a_purchase_order_with_valid_data(self):
        pass

    def navigate_to_the_purchase_order_list_or_details_page(self):
        pass

    def open_the_submitted_purchase_order_and_verify_all_details_match_the_data_entered_during_creation(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

