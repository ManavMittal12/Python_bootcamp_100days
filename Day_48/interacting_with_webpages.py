from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

_chrome_options = webdriver.ChromeOptions()
_chrome_options.add_experimental_option("detach", True)

_webdriver = webdriver.Chrome(options=_chrome_options)

# How to click on something.
_webdriver.get("https://en.wikipedia.org/wiki/Main_Page")
_webdriver.maximize_window()
# Getting the active editors
active_articles = _webdriver.find_element(By.CSS_SELECTOR, value='#mwDQ a')
# active_articles.click()     # Use click() method to click on the element.

# finding elements by link text - This is a find method that is very specific to links
all_portals = _webdriver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# typing something in search bar
# search_button = _webdriver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
# search_button.click()
search = _webdriver.find_element(By.NAME, value="search")
search.send_keys("Python")

# sending keyboard input to Selenium
# when we want to send a key that's not a letter or one of the numbers or symbols,
# we have to do a separate import
search.send_keys(Keys.ENTER)
#



# _webdriver.quit()
