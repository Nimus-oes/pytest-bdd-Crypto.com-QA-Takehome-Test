import pytest
import pytz
import selenium.webdriver
from datetime import datetime, timedelta
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage

# Settings for command line options
def pytest_addoption(parser):
    parser.addoption("--days", action="store", default=2, type=int, help="Number of days from now for api testing")

#-----------------------------------------------------------------------------------------------------------------#
# Fixtures for Crypto.com Exchange UI test (exchange.feature, test_exchange.py)

# Create browser instance
@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    # The default browser size is desktop
    b.set_window_size(1200, 891)
    yield b
    b.quit()


# Create Markets page instance using the browser instance
@pytest.fixture
def markets_page(browser):
    return ExchangeMarketsPage(browser)


# Create Pair page instance using the browser instance
@pytest.fixture
def pair_page(browser):
    return TradePairPage(browser)


#-----------------------------------------------------------------------------------------------------------------#
# Fixtures for Hong Kong Observatory API test (weather.feature, test_weather.py)

@pytest.fixture
def date_to_forecast(request):
    # By deafult, set the date for 2 days from now
    # If there is a days value provided via command line, use it instead
    days_from_now = request.config.getoption("--days")
    # Check if the provided number of days are valid
    assert isinstance(days_from_now, int) and 0 < days_from_now <= 9, f"Number of days can only be integers from 1 to 9. Provided value: {days_from_now}"
    
    # Get the date value of today in HKT
    hk_tz = pytz.timezone("Asia/Hong_Kong")
    today = datetime.now(hk_tz).date()

    # Caluclate the target date
    target_date = today + timedelta(days=days_from_now)

    # Format the target date so that it matches the format of the API response
    formatted_target_date = target_date.strftime("%Y%m%d")

    return formatted_target_date