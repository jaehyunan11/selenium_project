from selenium import webdriver
from selenium.webdriver.common.by import By
from handy_wrapper import HandWrappers
import time


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        hw = HandWrappers(driver)
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck(
            "//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()
