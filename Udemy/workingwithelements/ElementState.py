from selenium import webdriver
import time


class ElementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com/"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        e1 = driver.find_element_by_class_name("gLFyf")
        e1State = e1.is_enabled()  # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))

        # e2 = driver.find_element_by_class_name("gLFyf")
        # e2State = e2.is_enabled()  # True for enabled and False for disabled
        # print("E2 is Enabled? -> " + str(e2State))

        # e3 = driver.find_element_by_class_name("gLFyf")
        # e3State = e3.is_enabled()  # True for enabled and False for disabled
        # print("E3 is Enabled? -> " + str(e3State))

        e1.send_keys("letskodeit")

        time.sleep(3)


e = ElementState()
e.isEnabled()
