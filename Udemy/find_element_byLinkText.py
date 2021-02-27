from selenium import webdriver
import time


class FindByLinkText():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)

        elementByLinkText = driver.find_element_by_link_text('Login')

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        time.sleep(5)

        elementByPartialLinkText = driver.find_element_by_partial_link_text(
            'Pract')

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

        time.sleep(5)


cc = FindByLinkText()
cc.test()
