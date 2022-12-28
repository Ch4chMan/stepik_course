import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_language(browser):
    browser.get(link)
    button = browser.find_elements(By.XPATH, '/*[@id="add_to_basket_form"]/button')
    assert button is not None, "-----Omg, OMG! Where is his button?------\n" \
                           "---Where is the button? Where is the button? I wish I knew where...---"
    
    time.sleep(5)

if __name__ == "__main__":
    pytest.main()

