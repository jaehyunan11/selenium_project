from selenium import webdriver
import time


class FindByClassTag():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)

        elementByClassName = driver.find_element_by_class_name(
            "displayed-class")

        elementByClassName.send_keys("Testing the element")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        time.sleep(5)

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by Tag Name abd the text on element is:" + text)

        time.sleep(5)


cc = FindByClassTag()
cc.test()
