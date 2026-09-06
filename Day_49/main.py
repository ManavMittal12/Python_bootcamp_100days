from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "iambatman1@batcave.com"
ACCOUNT_PASSWORD = "Mark42inbound"

GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)


wait = WebDriverWait

button1 = driver.find_element(By.CLASS_NAME, "Home_heroButton__3eeI3")
button1.send_keys(Keys.ENTER)

email_entry = driver.find_element(By.NAME, "email")
password_entry = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.CLASS_NAME, "Login_submitButton__tJFna ")

email_entry.send_keys(ACCOUNT_EMAIL)
password_entry.send_keys(ACCOUNT_PASSWORD)
login_button.send_keys(Keys.ENTER)
