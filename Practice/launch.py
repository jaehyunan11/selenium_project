from selenium import webdriver
import time


class ChromeDriverMac():

    def test(self):
        # instantiate Chrome Browser Command
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        # Open the privded URL
        driver.get('http://www.google.com/')
        time.sleep(5)
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(5)
        driver.quit()


cc = ChromeDriverMac()
cc.test()
