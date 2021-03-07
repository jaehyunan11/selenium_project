import unittest
from Project_Framework.pages.home.login_page import Login_page
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = Login_page(driver)
        lp.login('jaehyuna11@gmail.com', 'jaeHYUN^^48625')

        userIcon = driver.find_element(
            By.XPATH,  ".//*[@id='navbar']//span[contains(text(), 'Jaehyun An')]")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        time.sleep(3)
