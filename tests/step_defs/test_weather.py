from pytest_bdd import scenarios, given, then
import requests

scenarios('../features/weather.feature')

@given("9-day weather forecast api is queried with 'dataType=fnd' and 'lang=en'", target_fixture='nine_day_response')
def nine_day_response():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    params = {"dataType": "fnd", "lang": "en"}
    response = requests.get(url, params)
    return response


@then("the response status code is '200'")
def nine_day_response_code(nine_day_response):
    status = nine_day_response.status_code
    assert status == 200, f"Unexpected status code: {status}"


# Date to forecast is returned from conftest.py with default value of 2 days from now
@then("the response contains maximum and minimum relative humidity for '2 days' from now")
def nine_day_response_humidity(nine_day_response, date_to_forecast):
    # Get 9-day forecast response data
    data = nine_day_response.json()
    weather_forecast = data["weatherForecast"]
    target_date_data = None

    # Loop through the data to find the matching date and assign its value to target_date_data
    for each in weather_forecast:
        if each["forecastDate"] == date_to_forecast:
            target_date_data = each
            break
    
    # Verify that there is a matching date in the API response
    # If not, raise an exception
    if target_date_data is None:
        raise Exception(f"No matching date found for {date_to_forecast}")
    
    # Get the relative humidity data of the target date
    max_rel_humidity = target_date_data["forecastMaxrh"]["value"]
    min_rel_humidity = target_date_data["forecastMinrh"]["value"]

    # Verify the humidity values
    assert max_rel_humidity >= 0, f"Maximum relative humidity value must be numbers. Current value: {max_rel_humidity}"
    assert min_rel_humidity >= 0, f"Minimum relative humidity value must be numbers. Current value: {min_rel_humidity}"