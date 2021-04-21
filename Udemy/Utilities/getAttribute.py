from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")
        print("Value of attribute is: " + result)

        time.sleep(2)
        driver.quit()


ff = GetAttribute()
ff.test()
