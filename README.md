# Crypto.com-QA-Takehome-Test with pytest-bdd

Below is the project overview and setup guide.

## Test Target
1. **Crypto.com Exchange Page Navigation Test**:   
Navigating to ZIL/USDT page from crypto.com/exchange/markets
2. **HKO Weather Forecast API Test**:  
Getting the relative humidity information for the day after tomorrow from the Hong Kong Observatory 9-day weather forecast API   
&nbsp;
## Test Scenarios
This test suite follows the Behavior Driven Development process
1. **Crypto.com Exchange Page Navigation Test**  
    - Given: the markets page is displayed on mobile or desktop screen
    - When: the user clicks UI to get into ZIL/USDT page
        - The test can be separated into multiple test cases as per the different entry points
    - Then: the redirected page contains 'ZIL_USDT' in its url path
    - And: the page title contains 'ZIL/USDT'
    - And: the toggle menu on top of the page refers to 'ZIL/USDT  
2. **HKO Weather Forecast API Test**  
    - Given 9-day weather forecast api is queried with 'dataType=fnd' and 'lang=en'
    - Then the response status code is '200'
    - And the response contains maximum and minimum relative humidity for '2 days' from now  
&nbsp;
## Test Design and Structures
Page Object Model (POM) design pattern and pytest-bdd framework are applied
  - `pages` contains the page objects for the markets and spot pair pages for Crypto.com Exchange test
  - `tests/features` contains each test feature that outlines the test scenario 
  - `tests/step_defs` contains scenario steps for each feature
  - `conftest.py` contains the shared fixtures  
&nbsp;
## Tech Stack
- Python 3
- pytest
- pytest-bdd
- requests
- Selenium
- Chrome WebDriver  
&nbsp;
## Supported Browser
- Google Chrome  
&nbsp;
## Test Cases by Feature - Crypto.com Exchange Page Navigation
1. `Navigate by the navigation items on markets page` scenario  
    - By **USDT** navigation menu on desktop
    - By **USDT** navigation menu on mobile
    - By **All** navigation menu on desktop
    - By **All** navigation menu on mobile
    - By **Favorites** navigation menu on desktop
    - By **Favorites** navigation menu on mobile 
2. `Navigate by the search section on top of the page` scenario
    - By top **search** section > **All** market tab on desktop
    - By top **search** section > **Spot** market tab on desktop  
3. `Navigate by the header navigation menu on top of the page` scenario
    - By **Trade** header > **Spot** sub header > **Toggle pair** item >  **USDT** navigation menu on desktop 
    - By **Burger** menu > **Trade** header > **Spot** sub header >  **Toggle pair** item >  **USDT** navigation menu on mobile
    - By **Trade** header > **Spot** sub header >  **Toggle pair** item >  **Favorites** navigation menu on desktop
    - By **burger** menu > **Trade** header > **Spot** sub header >  **Toggle pair** item >  **Favorites** navigation menu on mobile  
&nbsp;
## Test Cases by Feature - HKO Weather Forecast API
1. `Get the relative humidity forecast for 2 days from now` scenario
    - By **dataType=fnd** and **lang=en** queries  
&nbsp;
## Limits
The limitations imposed on Crypto.com Exchange page navigation tests.
- The test suite is specific to English language. Other language pages are not supported.
- The test suite is specific to ZIL/USDT trade pair only, and it does **not** cover any other pairs. 
- There are two ways to access favorites items for testing: (1) logging into an account and accessing its favorite items, (2) adding the item to favorites on the spot without login and accessing the favorites. This test suite does not cover the option 1.
- The test suite does not cover the 'Categories' option due to the technical issue that fails to show dropdown content.
- The test suite does not cover the footer Trade > Spot option due to the spot page inaccessible issue   
&nbsp;
## Setting Up the Project
### Prerequisites
Make sure these are already installed in your system
- Python 3
- pip
- Chrome WebDriver 
### Installing the Repo and Dependencies
**Step 1**: Open your terminal and navigate to the directory where you want to clone this repository
```
cd path/to/your/directory
```
**Step 2**: Clone this repository and navigate to the repository directory  
This might require your GitHub username and personal access tokens.
```
git clone https://github.com/Nimus-oes/pytest-bdd-Crypto.com-QA-Takehome-Test.git
```
```
cd pytest-bdd-Crypto.com-QA-Takehome-Test
```
**Step 3**: Create a virtual environment
```
python3 -m venv .venv
```
**Step 4**: Activate the virtual environment
```
source .venv/bin/activate
```
**Step 5** : Install the required packages from the cloned repository
```
pip install -r requirements.txt
```  
&nbsp;
## How to Run the Tests
### Run all tests in the test suite
```
python -m pytest
```    

### Run tests by tags
Run feature level tests with `exchange` and `weather` tags.
- All tests for Crypto.com Exchange Page Navigation (12 test cases)
```
python -m pytest -m exchange
```
- All tests for HKO Weather Forecast API (1 test case)
```
python -m pytest -m weather
```
Run scenario level tests with `exchange_nav`, `exchange_search`, `exchange_header`, and `humidity` tags.
```
python -m pytest -m {scenario_tags}
```
### Run all tests and save the report in html
```
python -m pytest --html={report_name}.html
```
### Run tests in parallel
```
python -m pytest -n {number_of_threds}
```  
### Run tests with different inputs
HKO Weather Forecast API can receive values for the date to forecast by specifying the number of days from now. If not set, default value is 2 days from now (the day after tomrrow).
```
python -m pytest --days={number_of_days_from_now}
```  
- Run weather test only with a specified date and print the date for verification
```
python -m pytest -m weather -s --days={number_of_days_from_now}
```  
&nbsp;
___  
&nbsp;
Below is the log for learnings and challenges that I had during this test development.  
&nbsp;
## How to Handle ElementNotInteractableException
During the test development, I found many errors related to Element Not Interactable Exception whenever the browser tries to interact with the elements. There are three major solutions to tackle this exception.
1. **Explicitly wait for the element to be interactable. Try adding more conditions for the wait if one is not enough.**
```
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ELEMENT_LOCATOR))
```
```
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ELEMENT_LOCATOR) and EC.element_to_be_clickable(ELEMENT_LOCATOR))
```
2. **Scroll the element into viewport. If the element is not visible enough due to the position on the page, scroll it into the center of viewport.**
```
driver.execute_script("arguments[0].scrollIntoView();", element)
```
```
driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
```
3. **Try different types of click method.**
```
element.click()
```
```
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)
```
```
driver.execute_script("arguments[0].click();", element)
```
```
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).move_to_element(element).click().perform()
```   
&nbsp;
## How to Find an SVG Element with XPath
In order to interact with an SVG element via XPath in Selenium, `name()` or `local-name()` method should be called. 
```
//*[name()='svg' and query]
```
```
//*[local-name()='svg' and query]
```   
&nbsp;
## Challenges and Solutions 
### Crypto.com Exchange Page Navigation Test
1. Markets page is not accessible from my location, South Korea presumably due to the geo restrictions
> **Solution**: Used VPN for testing. This resolved the access issue with Chrome browser  
> **Remaining issue**: Access issue still remains with Firefox browser and headless mode in both Chrome and Firefox even with VPN.
2. ElementNotInteractableException raised when clicking ZIL/USDT pair item
> **Solution**: Clicked the pair item with send_keys() method instead of click()
3. ElementNotInteractableException raised when clicking favorites star icon
> **Solution**: After scrolling the element into viewport, hard slept for 2 seconds for the element to be interactable. Although hard sleep is not recommended for efficient testing, there was no workable solution I could find other than this (explicit wait didn't work for this element)
4. ElementNotInteractableException raised when clicking favorites navigation item. The scrolling stopped at some point.
> **Solution**: After scrolling the element into viewport, hard slept for 2 seconds for the scroll to be completed.
5. Categories dropdown menu is not showing when clicked or mouse hovered
> **Solution**: No solution found yet. 
> 
> Tried explicit wait, hard sleep, ActionChain, and JavaScript to trigger the hover effect but none of it worked.
6. When tried to access footer Trade > Spot menu, the newly opened page is redirected to crypto.com/exchange again. Spot page is not accessible with footer navigation.
> **Solution**: No solution found yet. Tried to change the url again in the new window but didn't work.
### HKO Weather Forecast API Test
1. Target date not found in the response content when tried to fetch the data with index. The day after tomrrow was not always located in the index 1 item. 
> **Solution**: Fetching the data based on the index made the test vulnerable. Used for loop to find the matching date first. 
2. The location of contest.py made the command line option written inside the module unrecognizable. pytest seems to have some issues with recognizing the arguments when the conftest.py is deeply nested.
> **Solution**: 
> 1. Moving conftest.py into the root diretory when setting the command line option with pytest_addoption()
> 2. Using os.getenv() to set the command line option and leaving contest.py in the tests directory  
>
>    Used option 1 for this test.
3. KeyError occurred when there are multiple Examples tables in feature. Can't pass the parameter values with separate tables
> **Solution**: Provided all parameter values per record in one table  

&nbsp;
## Room for Improvements
### Crypto.com Exchange Page Navigation Test
The test suite can be improved to take spot trading pairs as varying inputs so that it can test any pair provided, making the suite more compatible and reusable.

### HKO Weather Forecast API Test
The test suite can be improved to test other values in the 9-day forecast response. 