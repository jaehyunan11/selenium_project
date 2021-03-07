from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class ListOfElements():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName -> Size of the list is: " + str(length1))

        time.sleep(5)

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> Size of the list is :" + str(length2))


cc = ListOfElements()
cc.test()
