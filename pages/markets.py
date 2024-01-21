"""
This module contains ExchangeMarketsPage,
the page object for the markets page of Crypto.com Exchange
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ExchangeMarketsPage:
    # Base Page URL
    # This page is accessible from certain countries only. VPN required.
    URL = "https://www.crypto.com/exchange/markets"

    # Locators
    COOKIES = (By.CSS_SELECTOR, "[title='Accept Cookies']")
    SPOT_TAB = (By.XPATH, "//button[contains(@class, 'e-button--medium is-text')][contains(., 'Spot')]")
    USDT_NAV = (By.XPATH, "//div[@class='e-tabs']/div/div/span[text()='USDT']")
    ALL_NAV = (By.XPATH, "//div[@class='e-tabs']/div/div/span[text()='All']")
    FAVORITES_NAV = (By.XPATH, "//div[@class='e-tabs']/div/div/span[text()='Favorites']")
    FAVORITES_ICON = (By.XPATH, "//*[name()='svg' and following-sibling::div/a[@href='/exchange/trade/ZIL_USDT']]")
    ZIL_USDT_PAIR_MAIN = (By.XPATH, "//a[@href='/exchange/trade/ZIL_USDT'][.//span[@class='base'][text()='ZIL']]")
    TOP_SEARCH_ICON = (By.XPATH, "//*[name()='svg' and @class='e-icon e-icon-search']")
    TOP_SEARCH_ALL = (By.XPATH, "//div[@class='e-tabs tabs']/div/div[contains(@class, 'e-tabs__nav-item')][span[text()='All']]")
    TOP_SEARCH_SPOT = (By.XPATH, "//div[@class='e-tabs tabs']/div/div[contains(@class, 'e-tabs__nav-item')][span[text()='Spot']]")
    ZIL_USDT_PAIR_SEARCH = (By.XPATH, "//div[@class='group-item']/a[@href='/exchange/trade/ZIL_USDT']/div[text()='ZIL/USDT']")
    TRADE_HEADER_DESKTOP = (By.XPATH, "//button[@class='link-btn e-button e-button--primary e-button--default is-text'][contains(., 'Trade')]")
    SPOT_HEADER_DESKTOP = (By.XPATH, "//div[@class='sub-menu']/a[@href='/exchange/trade?type=spot']")
    BURGER_MENU = (By.XPATH, "//*[name()='svg' and @class='e-icon e-icon-burger pointer']")
    TRADE_HEADER_MOBILE = (By.XPATH, "//span[@class='menu-name' and text()='Trade']")
    SPOT_HEADER_MOBILE = (By.XPATH, "//span[@class='sub-menu-name' and text()='Spot']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser


    # Set the screen size to mobile (default set to desktop in conftest.py)
    def set_mobile_screen(self):
        self.browser.set_window_size(360, 800)


    # Load the base page - crypto.com/exchange/markets
    def load(self):
        self.browser.get(self.URL)


    # Resources for verifying the base page url
    def url(self):
        return self.browser.current_url


    # Dismiss the cookie window
    def cookies(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.COOKIES))
        ck = self.browser.find_element(*self.COOKIES)
        ck.send_keys(Keys.RETURN)


    #----------------------------------MARKETS PAGE MAIN SECTION----------------------------------#

    # Find Spot market tab to verify or click it
    def spot_market_tab(self, action):
        spot = self.browser.find_element(*self.SPOT_TAB)
        if action == 'verify':
            class_value = spot.get_attribute("class")
            return class_value
        elif action == 'click':
            spot.click()
        else:
            raise Exception("Verify or click action argument required for spot_market_tab.")


    # Find and click USDT navigation menu under Spot market
    def usdt_nav(self):
        usdt = self.browser.find_element(*self.USDT_NAV)
        self.browser.execute_script("arguments[0].click();", usdt)


    # Find and click All navigation menu under Spot market
    def all_nav(self):
        nav_all = self.browser.find_element(*self.ALL_NAV)
        self.browser.execute_script("arguments[0].click();", nav_all)


    # Find and click Favorites navigation menu under Spot market
    def fav_nav(self):
        fav = self.browser.find_element(*self.FAVORITES_NAV)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", fav)
        self.browser.execute_script("arguments[0].click();", fav)


    # Find and click favorite icon next to ZIL/USDT pair to add to favorites
    def add_to_favorites(self):
        star = self.browser.find_element(*self.FAVORITES_ICON)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
        time.sleep(2)
        star.click()


    # Find and click ZIL/USDT pair item from the list on markets page
    def zil_pair_main(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.ZIL_USDT_PAIR_MAIN))
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR_MAIN)
        zil.send_keys(Keys.RETURN)


    #----------------------------------TOP SEARCH SECTION----------------------------------#
    
    # Hover the mouse over the search icon on top of the page when the screen size is desktop
    def top_search_icon(self):
        ts = self.browser.find_element(*self.TOP_SEARCH_ICON)
        ActionChains(self.browser).move_to_element(ts).perform()

    # Find 'All' market tab to verify or click it
    def top_search_all(self, action):
        market = self.browser.find_element(*self.TOP_SEARCH_ALL)
        if action == 'verify':
            class_value = market.get_attribute("class")
            return class_value
        elif action == 'click':
            market.click()
        else:
            raise Exception("Verify or click action argument required for top_search_all.")


    # Find and click Spot market tab from the top search section
    def top_search_spot(self):
        spot = self.browser.find_element(*self.TOP_SEARCH_SPOT)
        spot.click()


    # Find and click ZIL/USDT pair item from the top search section
    def zil_pair_search(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.ZIL_USDT_PAIR_SEARCH))
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR_SEARCH)
        zil.click()

    #----------------------------------HEADER NAV SECTION----------------------------------#
    
    # Find and click Trade header nav on desktop screen
    def header_nav_trade_desktop(self):
        trade = self.browser.find_element(*self.TRADE_HEADER_DESKTOP)
        ActionChains(self.browser).move_to_element(trade).perform()


    # Find and click Spot sub header under Trade on desktop screen
    def header_nav_spot_desktop(self):
        spot = self.browser.find_element(*self.SPOT_HEADER_DESKTOP)
        spot.click()


    # Find and click burger menu icon on mobile screen
    def header_burger_mobile(self):
        burger = self.browser.find_element(*self.BURGER_MENU)
        burger.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.TRADE_HEADER_MOBILE))


    # Find and click Trade header nav on mobile screen
    def header_nav_trade_mobile(self):
        trade = self.browser.find_element(*self.TRADE_HEADER_MOBILE)
        trade.click()
        time.sleep(1)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SPOT_HEADER_MOBILE))


    # Find and click Spot sub header under Trade on mobile screen
    def header_nav_spot_mobile(self):
        spot = self.browser.find_element(*self.SPOT_HEADER_MOBILE)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(spot))
        spot.click()