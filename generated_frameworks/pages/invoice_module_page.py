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

    def navigate_to_the_invoice_module(self):
        pass

    def click_on_the_invoice_history_section_or_tab(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def observe_the_list_of_invoices_displayed(self):
        pass

    def access_the_invoice_history_section(self):
        pass

    def verify_that_invoices_are_displayed_in_chronological_order(self):
        pass

    def check_for_pagination_or_scrolling_if_there_are_many_invoices(self):
        pass

    def select_an_invoice_from_the_invoice_list(self):
        pass

    def click_on_the_generate_pdf_or_download_pdf_button(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def wait_for_the_pdf_to_be_generated_and_downloaded(self):
        pass

    def open_the_downloaded_pdf_file(self):
        pass

    def access_the_invoice_module(self):
        pass

    def choose_an_invoice_from_the_history_list(self):
        pass

    def click_on_the_option_to_download_the_invoice_as_pdf(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def verify_the_download_progress_and_completion(self):
        pass

    def open_the_downloaded_pdf_and_verify_content_formatting_and_accuracy(self):
        pass

    def select_an_invoice_to_be_emailed(self):
        pass

    def click_on_the_email_invoice_button_or_link(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def enter_the_customers_email_address_if_not_prefilled(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

    def click_send_to_email_the_invoice(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def verify_confirmation_message_for_successful_email_sending(self):
        pass

    def open_the_invoice_module(self):
        pass

    def select_an_invoice_from_the_list(self):
        pass

    def click_on_email_invoice(self):
        self.safe_click(
            "UNKNOWN",
            ['UNKNOWN']
        )

    def verify_the_email_form_appears_with_customers_email_prepopulated_or_enter_a_valid_email(self):
        self.safe_fill(
            "UNKNOWN",
            "test_data",
            ['UNKNOWN']
        )

    def send_the_invoice_via_email(self):
        pass

    def check_for_success_notification_and_verify_email_receipt_by_the_customer(self):
        pass

