@exchange
Feature: Crypto.com Exchange ZIL/USDT Trade Pair Page
  As a Crypto.com Exchange user,
  I want to navgiate to the spot trading page of 'ZIL/USDT'
  So I can check the pair data and proceed with the trading

  @exchange_nav
  Scenario Outline: Navigate by the navigation items on markets page
    Given the markets page is displayed on '<screen_size>' screen
    When I click '<nav_item>' under the Spot market and click the 'ZIL/USDT' pair item among the list
    Then the pair in toggle menu on top of the redirected page refers to 'ZIL/USDT'
    And the page contains 'ZIL_USDT' in its url path
    And the page title contains 'ZIL/USDT'

    Examples: Nav
    |  nav_item  |  screen_size  |
    |  USDT      |  desktop      |
    |  USDT      |  mobile       |   
    |  All       |  desktop      |
    |  All       |  mobile       |
    |  Favorites |  desktop      |
    |  Favorites |  mobile       |   


  @exchange_search
  Scenario Outline: Navigate by the search section on top of the page
    Given the markets page is displayed on 'desktop' screen
    When I click 'search icon' on top of the page, '<market>' nav menu in the dropdown content, and 'ZIL/USDT' pair item among the list
    Then the pair in toggle menu on top of the redirected page refers to 'ZIL/USDT'
    And the page contains 'ZIL_USDT' in its url path
    And the page title contains 'ZIL/USDT'

    # This is desktop-only test
    Examples: Market
    |  market  |
    |  All     |
    |  Spot    |


  @exchange_header
  Scenario Outline: Navigate by the header navigation menu on top of the page
    Given the markets page is displayed on '<screen_size>' screen
    When I click 'Trade' menu on top of the page, and 'Spot' sub-menu in the dropdown content
    And in the redirected page, I click the pair toggle, '<nav_item>' on top, and 'ZIL/USDT' pair item
    Then the pair in toggle menu on top of the redirected page refers to 'ZIL/USDT'
    And the page contains 'ZIL_USDT' in its url path
    And the page title contains 'ZIL/USDT'

    Examples: Header
    |  nav_item  |  screen_size  |
    |  USDT      |  desktop      |
    |  USDT      |  mobile       |   
    |  Favorites |  desktop      |
    |  Favorites |  mobile       |   
