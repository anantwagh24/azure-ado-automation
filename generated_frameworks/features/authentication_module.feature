Feature: Authentication Module

Scenario: Verify that username field is mandatory on login page
  Given Leave the username field empty
  And Enter a valid password
  When Click on the login button
  Then Validation message is displayed indicating that the username field is mandatory

Scenario: Verify that password field is mandatory on login page
  Given Enter a valid username
  And Leave the password field empty
  When Click on the login button
  Then Validation message is displayed indicating that the password field is mandatory

Scenario: Verify validation messages are shown when both username and password fields are empty
  Given Leave the username field empty
  And Leave the password field empty
  When Click on the login button
  Then Validation messages are displayed indicating that both username and password fields are mandatory

Scenario: Verify error message is shown when invalid credentials are entered
  Given Enter an invalid username
  And Enter an invalid password
  When Click on the login button
  Then Error message is displayed indicating invalid credentials

Scenario: Verify user is redirected to dashboard after successful login
  Given Enter a valid username
  And Enter a valid password
  When Click on the login button
  Then User is redirected to the dashboard page

Scenario: Verify session is created after successful login
  Given Enter a valid username
  And Enter a valid password
  When Click on the login button
  Then A user session is created and maintained after successful login

