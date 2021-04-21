from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from handy_wrapper import HandWrappers


class UsingWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        hw = HandWrappers(driver)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")

        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()
