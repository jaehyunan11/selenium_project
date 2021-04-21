from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: ", elementText)
        time.sleep(2)
        driver.quit()


ff = GetText()
ff.test()
