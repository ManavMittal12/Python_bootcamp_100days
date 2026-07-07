from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_option)
driver.get(
    "https://www.amazon.in/AULA-F75-Mechanical-Swappable-Pre-lubed/dp/B0CYZHC69C/ref=sr_1_1_sspa?crid=2H8ZTIFAO3UT&dib=eyJ2IjoiMSJ9.9lLTZbgIbyKbdcSuQyasW4QrIVGz42bDb4IfDYI8iHbg5Kt9edGc32ZwWCouJaanAbPPNCN8SyiK0CA2hNwG_LvPIQDatKZoKtj7d822oKRbT_-cuUy-QbdVIiUEOi5GUXvDr1FZOXtB26DsjMjTGb_723HqQFkYGvv7A3i-3WgLub--eGW8A8Sg2tyEU0rGPPSJ_nJ320j9Sq4N42yL8VjddZZ2DzVnVVjU2gDDvic.jUbUn1z_9H3CD1lMzDsRjPqlB2_D5-OwMn8d3ZjyTew&dib_tag=se&keywords=aula%2Bf75%2Bkeyboard&nsdOptOutParam=true&qid=1783443667&sprefix=%2Caps%2C462&sr=8-1-spons&aref=TviUf7meE3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
)


# it's the HTML element. We have to access the text content. we just have to add .text
price_rupee = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
print(f"The current price of the keyboard is : {price_rupee}₹")


# Beautiful soup is good for grabbing, scrapping data, but get's stuck when the
# website is being rendered by javascript or Angular or React and the content
# that was HTML was taking time to load, or requires certain conditions to load.



driver.quit()
