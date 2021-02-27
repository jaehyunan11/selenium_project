from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class ByDemo():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by ID")

        time.sleep(5)

        elementByXpath = driver.find_element(
            By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        time.sleep(5)

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by LinkText")

        time.sleep(5)


cc = ByDemo()
cc.test()
