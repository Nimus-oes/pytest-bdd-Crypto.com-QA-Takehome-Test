from sqlite3 import converters

from pytest import mark
from pytest_bdd import scenarios, parsers, given, when, then
import time
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage

scenarios('../features/exchange.feature')

CONVERTERS = {
    'nav_item': str,
    'screen_size': str,
    'market': str,
}

@given(parsers.parse("the markets page is displayed on '{screen_size}' screen"), converters=CONVERTERS, target_fixture='screen_size')
def load_markets(markets_page, screen_size):
    # Set the screen size. Default is desktop which is set in conftest.py
    if screen_size == 'desktop':
        pass
    elif screen_size == 'mobile':
        markets_page.set_mobile_screen()
    else:
        raise Exception(f"Screen size value can be either 'desktop' or 'mobile'. Current value: {screen_size}")
    
    # Load the markets page
    markets_page.load()
    # Dismiss the cookies window for better interaction with the pages
    markets_page.cookies()

    # Verify the url
    assert 'markets' in markets_page.url(), "Markets page not accessible"
    
    # Return screen size value for future use
    return screen_size


@when(parsers.parse("I click '{nav_item}' under the Spot market and click the 'ZIL/USDT' pair item among the list"), converters=CONVERTERS)
def click_pair_ui(markets_page, nav_item):
    # Verify that default market tab on the page is set to 'Spot'
    # If not, click the Spot market tab
    try:
        assert 'active' in markets_page.spot_market_tab('verify')
    except:
        markets_page.spot_market_tab('click')

    # Click navigation menu    
    if nav_item == 'USDT':
        markets_page.usdt_nav()
    elif nav_item == 'All':
        markets_page.all_nav()
    elif nav_item == 'Favorites':
        # From all pairs, find ZIL/USDT and add it to favorties
        markets_page.all_nav()
        markets_page.add_to_favorites()
        # Click Favorites navigation menu to see the added pair
        markets_page.fav_nav()
    else:
        raise Exception(f"Navigation item can only be 'USDT', 'All', or 'Favorites'. Current value: {nav_item}")

    # Scroll to ZIL/USDT pair and click it
    markets_page.zil_pair_main()
    

@when(parsers.parse("I click 'search icon' on top of the page, '{market}' nav menu in the dropdown content, and 'ZIL/USDT' pair item among the list"), converters=CONVERTERS)
def click_top_search(markets_page, market):
    # Click the search icon on top of the page
    markets_page.top_search_icon()

    if market == 'All':
        # Verify the default market tab is set to 'All'
        # If not, click the 'All' market tab
        try:
            assert 'active' in markets_page.top_search_all('verify')
        except:
            markets_page.top_search_all('click')
    elif market == 'Spot':
        markets_page.top_search_spot()
    else:
        raise Exception(f"Market value can be either 'All' or 'Spot'. Current value: {market}")
    
    # Scroll to ZIL/USDT pair and click it
    markets_page.zil_pair_search()


@when("I click 'Trade' menu on top of the page, and 'Spot' sub-menu in the dropdown content")
def click_header_spot(markets_page, screen_size):
    if screen_size == 'desktop':
        # Click Trade header nav menu on desktop
        markets_page.header_nav_trade_desktop()
        # Click Spot sub header menu under Trade on desktop
        markets_page.header_nav_spot_desktop()
    else:
        # Click the burger menu icon on mobile
        markets_page.header_burger_mobile()
        # Click the Trade header nav on mobile
        markets_page.header_nav_trade_mobile()
        # Click the Spot sub header menu under Trade on mobile
        markets_page.header_nav_spot_mobile()


@when(parsers.parse("in the redirected page, I click the pair toggle, '{nav_item}' on top, and 'ZIL/USDT' pair item"), converters=CONVERTERS)
def click_pair_toggle(pair_page, nav_item):
    # Hover the mouse over the toggle menu on top to change the pair item
    pair_page.top_pair('select')
    # Click the USDT navigation tab
    pair_page.usdt_nav()
    if nav_item == 'Favorites':
        # Click favorite star icon to add the pair to the favorites
        pair_page.add_to_favorites()
        # Click the Favorites navigation tab
        pair_page.fav_nav()
    # Click ZIL/USDT pair item
    pair_page.zil_pair_toggle()


@then("the pair in toggle menu on top of the redirected page refers to 'ZIL/USDT'")
def verify_toggle_pair(pair_page):
    # Verify the pair in the toggle menu. Desired text format is 'ZIL/USDT'
    assert 'ZIL/USDT' in pair_page.top_pair('verify'), "The pair not found on toggle menu"


@then("the page contains 'ZIL_USDT' in its url path")
def verify_url(pair_page):
    # Verify the page URL. Desired URL format is "https://crypto.com/exchange/trade/ZIL_USDT"
    assert 'ZIL_USDT' in pair_page.page_url(), "The page URL doesn't match the pair"


@then("the page title contains 'ZIL/USDT'")
def verify_title(pair_page):
    # Verify the page title. Desired title format is "{price_value} | ZIL/USDT | Spot | Crypto.com Exchange"
    print(pair_page.page_title())
    assert 'ZIL/USDT' in pair_page.page_title(), "The page title doesn't match the pair"