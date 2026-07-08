from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email= driver.find_element(By.NAME, value="email")

# Fill the form
f_name.send_keys("Bruce")

l_name.send_keys("Wayne")
email.send_keys("iambatman@gmail.com")

submit_button = driver.find_element(By.CSS_SELECTOR, value="button")
submit_button.click()
