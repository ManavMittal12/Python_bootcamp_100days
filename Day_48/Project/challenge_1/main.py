from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver = webdriver.ChromeOptions()
chrome_driver.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_driver)
driver.get("https://www.python.org/")

events_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_info = {}
for time, name in zip(events_times, event_names):
    event_info[time.text] = name.text

print(event_info)

driver.quit()
