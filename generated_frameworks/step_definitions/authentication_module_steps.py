from behave import given, when, then

@given("Leave the Username field empty")
def leave_the_username_field_empty(context):
    pass

@given("Enter a valid password in the Password field")
def enter_a_valid_password_in_the_password_field(context):
    pass

@when("Click on the Login button")
def click_on_the_login_button(context):
    pass

@then("Validation message is displayed indicating that the Username field is mandatory")
def validation_message_is_displayed_indicating_that_the_username_field_is_mandatory(context):
    pass

@given("Enter a valid username in the Username field")
def enter_a_valid_username_in_the_username_field(context):
    pass

@given("Leave the Password field empty")
def leave_the_password_field_empty(context):
    pass

@then("Validation message is displayed indicating that the Password field is mandatory")
def validation_message_is_displayed_indicating_that_the_password_field_is_mandatory(context):
    pass

@given("Enter an invalid username in the Username field")
def enter_an_invalid_username_in_the_username_field(context):
    pass

@given("Enter an invalid password in the Password field")
def enter_an_invalid_password_in_the_password_field(context):
    pass

@then("An error message is displayed indicating invalid credentials")
def an_error_message_is_displayed_indicating_invalid_credentials(context):
    pass

@then("User is redirected to the dashboard page")
def user_is_redirected_to_the_dashboard_page(context):
    pass

@when("Verify session or authentication token is created")
def verify_session_or_authentication_token_is_created(context):
    pass

@then("A session or authentication token is created and maintained for the logged-in user")
def a_session_or_authentication_token_is_created_and_maintained_for_the_loggedin_user(context):
    pass

@given("Leave both Username and Password fields empty")
def leave_both_username_and_password_fields_empty(context):
    pass

@then("Validation messages are displayed indicating that both Username and Password fields are mandatory")
def validation_messages_are_displayed_indicating_that_both_username_and_password_fields_are_mandatory(context):
    pass

