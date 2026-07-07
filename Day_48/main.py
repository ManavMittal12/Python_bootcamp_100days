from selenium import webdriver


# this web-driver will drive the chromium


# Now, we have selenium webdriver and browsers,
# we want to make sure that our driver is using chrome,
# we need a bridge in between, that bridge is provided
# by the chrome driver
# there will be different drivers for other browsers.

# Keep the browser open after program finishes

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")

# driver.close()  # just closes the single tab
# driver.quit() # quits entire browser
