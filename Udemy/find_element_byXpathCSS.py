from selenium import webdriver
import time


class FindByXpathCss():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        time.sleep(5)

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element by CSS")

        time.sleep(5)


cc = FindByXpathCss()
cc.test()
