from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


# Python Selenium automation using Google Chrome Browser
class PiyushChrome:
    username = "standard_user"
    password = "standard_user"

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # rendering the webpage on Google Chrome
    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
            self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
            self.driver.find_element(by=By.ID, value="login-button").click()
            print(self.driver.title)
            print(self.driver.current_url)
            page_content = self.driver.page_source
            with open('Webpage_Task_11.txt', 'w', encoding='utf-8') as file:
                file.write(page_content)

        except NoSuchElementException as selenium_error:
            print("element not found ", selenium_error)
        finally:
            self.driver.quit()


url = "https://www.saucedemo.com/"

suman = PiyushChrome(url)

suman.login()
