import dotenv
import os
import requests
from bs4 import BeautifulSoup
import smtplib


dotenv.load_dotenv(".env")
URL : str = "https://www.amazon.in/AULA-F75-Mechanical-Swappable-Pre-lubed/dp/B0CQXNQYFP/ref=sr_1_1_sspa?crid=2X3H59BREUFTU&dib=eyJ2IjoiMSJ9.9lLTZbgIbyKbdcSuQyasW4QrIVGz42bDb4IfDYI8iHbg5Kt9edGc32ZwWCouJaanAbPPNCN8SyiK0CA2hNwG_LvPIQDatKZoKtj7d822oKRbT_-cuUy-QbdVIiUEOi5GUXvDr1FZOXtB26DsjMjTGU1rAUQ_XBOtfNpsM1Wt3nUGxRu1S3w6qXBK0wFUAYJLPPSJ_nJ320j9Sq4N42yL8VjddZZ2DzVnVVjU2gDDvic.sfUxgaGNYCMsUAIyoiMW4E_rksv3ZL1li7v5n_COvx4&dib_tag=se&keywords=aula%2Bf75%2Bkeyboard&nsdOptOutParam=true&qid=1783440011&sprefix=aula%2Caps%2C260&sr=8-1-spons&aref=TviUf7meE3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
EMAIL : str = os.getenv("email")
PASSWORD : str = os.getenv("google_cred")

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()
item_price = float(soup.find(name="span", class_="a-price-whole").get_text().replace(",","").replace(".",""))

if item_price < 5000:
    message = f"Subject: Amazon Price Alert!\n\n{product_name} is now at {item_price}.Rs".encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=message
    )
