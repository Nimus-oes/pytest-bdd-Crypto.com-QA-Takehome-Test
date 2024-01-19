Feature: Hong Kong Observatory 9-day weather forecast API
  As a test automation engineer,
  I want to automate the api test for 9-day weather forecast of Hong Kong Observatory
  So I can make sure I get the forecast information anytime, anywhere.

  Scenario: Get the relative humidity forecast for 2 days from now
    Given 9-day weather forecast api is queried with 'dataType=fnd' and 'lang=en'
    Then the response status code is '200'
    And the response contains maximum and minimum relative humidity for '2 days' from now