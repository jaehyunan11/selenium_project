from selenium import webdriver
import time


class FindByIdName():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by ID")

        time.sleep(5)

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("we found an element by Name")

        time.sleep(5)

        driver.get("https://www.yahoo.com/")
        elementByClass = driver.find_element_by_class_name("_yb_jvztu")

        if elementByClass is not None:
            print("We found an element by Class")

        time.sleep(5)


cc = FindByIdName()
cc.test()
