from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # find all handles, there should two handels after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to_window(handle)
                print("Switched to window: " + handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break
        # Switch back to the parent handle
        driver.switch_to_window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successfully")

        # searchBox = driver.find_element(By.ID, "search-courses")
        # searchBox.send_keys("python")


ff = SwitchToWindow()
ff.test()
