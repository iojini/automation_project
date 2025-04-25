Feature: Test Scenario to Change Language

  Scenario: User can change the language from the page
    Given user navigates to the login page
    And user logs in with email and password
    And user clicks on the settings icon
    When user clicks on language icon
    And user selects the Russian language option
    Then the current language selected should be Russian