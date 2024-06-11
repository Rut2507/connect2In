from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class LinkedInBot:
    def __init__(self, username, password, keywords, num_pages):
        self.username = username
        self.password = password
        self.keywords = [kw.strip() for kw in keywords.split(',')]
        self.num_pages = num_pages
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys(self.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(3)

    def logout(self):
        all_buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for btn1 in all_buttons:
            if btn1.text == "Me":
                self.driver.execute_script("arguments[0].click();", btn1)
                time.sleep(2)
                signout_button = self.driver.find_element(By.XPATH,'//*[text()="Sign Out"]')
                signout_button.click()
                time.sleep(3)

    def search_and_connect(self, keyword):
        for page in range(1, self.num_pages + 1):
            self.driver.get(f'https://www.linkedin.com/search/results/people/?keywords={keyword}&page={page}')
            time.sleep(3)
            all_buttons = self.driver.find_elements(By.TAG_NAME,'button')
            for btn in all_buttons:
                if btn.text == "Connect":
                    try:
                        self.driver.execute_script("arguments[0].click();", btn)
                        time.sleep(2)
                        send = self.driver.find_element(By.XPATH,'//button[@aria-label="Send without a note"]')
                        self.driver.execute_script("arguments[0].click();", send)
                        close = self.driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]')
                        self.driver.execute_script("arguments[0].click();", close)
                        time.sleep(2)

                    except NoSuchElementException:
                        pass
                    except Exception as e:
                        print(e)

    def run(self):
        self.login()
        for keyword in self.keywords:
            self.search_and_connect(keyword)
        self.logout()
        self.driver.quit()
