from selenium import webdriver
import time


class RadioButtonsAndCheckBoxes():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        # It trys to wait 10sec before fail
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheckBox = driver.find_element_by_id("bmwcheck")
        bmwCheckBox.click()

        time.sleep(2)

        benzCheckBox = driver.find_element_by_id("benzcheck")
        benzCheckBox.click()

        print("BMW Radio Button is selected " +
              str(bmwRadioBtn.is_selected()))  # True if selected, False is not selected
        print("Benz Radio Button is selected " +
              str(benzRadioBtn.is_selected()))  # True if selected, False is not selected
        print("BMW CheckBox is selected " +
              str(bmwCheckBox.is_selected()))  # True if selected, False is not selected
        print("Benz CheckBox is selected " +
              str(benzCheckBox.is_selected()))  # True if selected, False is not selected


ff = RadioButtonsAndCheckBoxes()
ff.test()
