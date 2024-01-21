"""
This module contains TradePairPage,
the page object for the spot pair page of Crypto.com Exchange
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class TradePairPage:
    # Locators
    TOP_PAIR_TOGGLE = (By.CSS_SELECTOR, "div.toggle")
    TOGGLE_USDT_NAV = (By.XPATH, "//div[@class='e-tabs__nav plain']/div/span[text()='USDT']")
    FAVORITES_ICON = (By.XPATH, "//div[@role='listitem']/a[@href='/exchange/trade/ZIL_USDT']/div/*[name()='svg']")
    FAVORITES_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='Favorites']")
    DROPDOWN_BOX = (By.XPATH, "//div[@class='virtual-list custom-scrollbar']")
    ZIL_USDT_PAIR = (By.XPATH, "//a[@href='/exchange/trade/ZIL_USDT']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser


    # Resources for verifying the page title contains 'ZIL/USDT'
    def page_title(self):
        return self.browser.title


    # Resources for verifying the page url contains 'ZIL_USDT'
    def page_url(self):
        return self.browser.current_url


    # Find the pair in the toggle menu to verify or hover the mouse over it
    def top_pair(self, action):
        # Wait for the top toggle menu
        WebDriverWait(self.browser, 20).until(EC.text_to_be_present_in_element(self.TOP_PAIR_TOGGLE, '/'))
       
        # After loading all elements, find the element
        toggle = self.browser.find_element(*self.TOP_PAIR_TOGGLE)

        if action == 'verify':
            return toggle.text
        elif action == 'select':
            ActionChains(self.browser).move_to_element(toggle).perform()
        else:
            raise Exception("Verify or select action argument required for top_pair.")
        

     # Find and click USDT nav menu inside the pair toggle
    def usdt_nav(self):
        nav = self.browser.find_element(*self.TOGGLE_USDT_NAV)
        nav.click()


    # Find and click Favorites nav menu inside the pair toggle
    def fav_nav(self):
        fav = self.browser.find_element(*self.FAVORITES_NAV)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.ZIL_USDT_PAIR))
        fav.click()


    # Find and click favorite icon next to ZIL/USDT pair to add to favorites
    def add_to_favorites(self):
        box = self.browser.find_element(*self.DROPDOWN_BOX)
        self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", box)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located(self.ZIL_USDT_PAIR))
        star = self.browser.find_element(*self.FAVORITES_ICON)
        star.click()


    # Find and click ZIL/USDT pair item from the list inside the pair toggle
    def zil_pair_toggle(self):
        box = self.browser.find_element(*self.DROPDOWN_BOX)
        self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", box)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located(self.ZIL_USDT_PAIR))
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR)
        zil.click()