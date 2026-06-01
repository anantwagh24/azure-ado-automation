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

    def navigate_to_the_refund_request_creation_page(self):
        pass

    def select_a_cancelled_order_from_the_list_of_orders(self):
        pass

    def fill_in_the_required_refund_request_details(self):
        pass

    def submit_the_refund_request(self):
        pass

    def attempt_to_select_a_noncancelled_order_for_refund_request(self):
        pass

    def try_to_fill_in_refund_request_details_and_submit(self):
        pass

    def navigate_to_refund_request_creation_page(self):
        pass

    def select_an_order_for_refund_request(self):
        pass

    def system_automatically_validates_refund_eligibility_based_on_business_rules(self):
        pass

    def attempt_to_submit_the_refund_request(self):
        pass

    def navigate_to_the_refund_request_details_page(self):
        pass

    def open_the_recently_created_refund_request(self):
        pass

    def verify_all_entered_details_are_correctly_saved_and_displayed(self):
        self.safe_fill(
            "UNKNOWN",
            self.test_data_service.generate_test_data(step),
            ['UNKNOWN']
        )

    def access_the_audit_trail_or_history_log_for_the_refund_request(self):
        pass

    def verify_that_an_entry_exists_for_the_creation_of_the_refund_request(self):
        pass

    def check_details_such_as_timestamp_user_who_created_the_request_and_action_performed(self):
        pass

