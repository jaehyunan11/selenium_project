from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from explicit_wait_type import ExlicityWaitType


class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        wait = ExlicityWaitType(driver)
        driver.get(baseUrl)

        driver.find_element(By.ID, "").click()

        # wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        #                      NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

        # element = wait.until(EC.element_to_be_clickable(
        #     (By.ID, "stopfilter_steps-0")))

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()
