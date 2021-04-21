from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        loginLink = driver.find_element(
            By.XPATH, "//a[contains(text(),'Login')]")
        loginLink.click()

        time.sleep(3)

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        time.sleep(3)


ff = ImplicitWaitDemo()
ff.test()
