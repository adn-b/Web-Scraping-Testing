from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Opens the browser in maximized mode
options.add_argument("--disable-notifications")  # Disables browser notifications
driver = webdriver.Chrome(options=options)


url = "https://temp-mail.org/"
driver.get(url)

def captcha():
    try:
        time.sleep(5)

        wait = WebDriverWait(driver, 10)  # Timeout after 10 seconds
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'https://challenges.cloudflare.com/')]")))
        print("JIFJSIF:",iframe)
        driver.switch_to.frame(iframe)
        print("Switched to iframe.")

        checkbox_xpath = "//html/body/div[@class='main-wrapper']/div[@id='content']/div[@id='challenge-stage']//input[@type='checkbox']"
        checkbox = driver.find_element(By.XPATH, checkbox_xpath)
        print("Text:",checkbox)
        checkbox.click()
        print("Checkbox clicked")

        time.sleep(2)

    except Exception as e:
        print(f"Error handling conditions: {e}")
    finally:
        driver.switch_to.default_content()

while True:
    try:
        body_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'no-js'))
            )
        print("Element 'no-js' is present. Handling conditions.")
        time.sleep(5)
        # print("Re-doing CAPTCHA.")
        captcha()
    except TimeoutException:
        print("Success!")
        # break
    time.sleep(5)