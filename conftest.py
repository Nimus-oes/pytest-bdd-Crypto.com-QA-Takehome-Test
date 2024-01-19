import pytest
from datetime import datetime, timedelta
import pytz

def pytest_addoption(parser):
    parser.addoption("--days", action="store", default=2, type=int, help="Number of days for testing")

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