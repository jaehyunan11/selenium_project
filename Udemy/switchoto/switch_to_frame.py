from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0,1000);")

        # Switch to frame using ID

        driver.switch_to_frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to_frame("iframe-name")

        # Switch to frame using number
        # first page
        # driver.switch_to_frame(0)

        time.sleep(2)
        # Search Course
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        # Switch back to the parent handle
        driver.switch_to_default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToFrame()
ff.test()
