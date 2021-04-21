from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXPathFormat():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        # Login -> Lecture "how to clikc and type on a web element"
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        email = driver.find_element(By.ID, "user_email")
        time.sleep(3)
        email.send_keys("jaehyuna11@gmail.com")
        time.sleep(3)
        password = driver.find_element(By.ID, "user_password")
        time.sleep(3)
        password.send_keys("jaeHYUN^^48625")
        time.sleep(3)
        driver.find_element(By.NAME, "commit").click()

        time.sleep(3)

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        time.sleep(3)

        # Select Course

        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


ff = DynamicXPathFormat()
ff.test()
