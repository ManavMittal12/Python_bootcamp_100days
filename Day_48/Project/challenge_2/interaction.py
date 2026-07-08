from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Setting up the driver
webdriver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
webdriver.get("https://en.wikipedia.org/wiki/Main_Page")

# Getting the active editors
active_editors = webdriver.find_element(By.XPATH, value='//*[@id="mwCw"]').text
print(f"Wikipedia has {active_editors} active editors.")

webdriver.quit()
