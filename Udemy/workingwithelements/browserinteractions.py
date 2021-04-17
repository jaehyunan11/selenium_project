from selenium import webdriver
import time


class BrowserInteractions():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(
            '/Users/jaehyunan/Desktop/Selenium/chromedriver')
        driver.get(baseURL)

        # Window Maximize
        driver.maximize_window()

        time.sleep(3)

        # Open the URL
        driver.get(baseURL)

        time.sleep(3)

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)

        time.sleep(3)

        # Get current URL
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)

        time.sleep(3)

        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        time.sleep(3)

        # Open another URL
        driver.get(
            "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        time.sleep(3)

        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        time.sleep(3)

        # Browser Forward
        driver.forward()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        time.sleep(3)

        # Get Page Source
        pageSource = driver.page_source
        print(pageSource)

        time.sleep(3)

        # Browser Close / Quit
        # driver.close()
        driver.quit()


cc = BrowserInteractions()
cc.test()
