from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)   # This will print it as a selenium element rather than an HTML
# print(search_bar.tag_name)   # If we want to access it's various attributes or text or tag name
# then we have to use a "." and tag_name or get_attribute() and the value of the attribute we want.
# we can find an element by name, class and id. we can also find the
# css selector as well

button = driver.find_element(By.ID,value="submit")
print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)

# if all else fails, we can use XPath, it's a way of getting a CSS element
# using a path structure (just like path)
# eg
# /html/body/div/ul/li

# using xpath
# select the element in to inspect --> copy --> copy XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[3]/ul/li[1]/a')
print(bug_link.text)
# https://www.w3schools.com/xml/xpath_intro.asp

driver.quit()
