from bs4 import BeautifulSoup
import smtplib
import requests
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv()) #Take environment variables from .env

SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
URL = "https://www.amazon.com/Ninestars-DZT-50-13-Automatic-Touchless-Stainless/dp/B00K2VKFSE/ref=sr_1_4?crid=1LA78ZJIUFNYO&dib=eyJ2IjoiMSJ9.5Bxy4IpDIx1FT0PxQhBrbE1oKh9tm8p6kcHiuF6IdvEMkiVc6yw2VO3B_8rE9-K9V5M5k6QYLjboRkzbKsaJmCGEEH2RQy_B_5SzpdKNXjexIZMnDsLRwXdZRf-vXCVbZ4ymupVuVFyTXqueOlfKTjXAoGOPsiLvuCfKfsFdqxEhcrJtgalGWHx1rAcvktxfYUs1Nm_b4SN2kH3an9xuzllkvUjY2XNWLykAgMOwVNMtPsQn9p6CY5IRO13ZX5-5AX-GfsF0VSjOIJT77tc9iv3XwdNPZuwmRRikPBfpUEw.r1_PqhlNOE7qBsyvxfweGY_jR6g47EEwZrQdWYQ4RyY&dib_tag=se&keywords=AUTOMATIC%2BTRASH%2Bcan&qid=1723668032&s=home-garden&sprefix=automatic%2Btrash%2Bca%2Cgarden%2C500&sr=1-4&th=1"

print(SMTP_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD)


response = requests.get("https://www.amazon.com/Ninestars-DZT-50-13-Automatic-Touchless-Stainless/dp/B00K2VKFSE/ref=sr_1_4?crid=1LA78ZJIUFNYO&dib=eyJ2IjoiMSJ9.5Bxy4IpDIx1FT0PxQhBrbE1oKh9tm8p6kcHiuF6IdvEMkiVc6yw2VO3B_8rE9-K9V5M5k6QYLjboRkzbKsaJmCGEEH2RQy_B_5SzpdKNXjexIZMnDsLRwXdZRf-vXCVbZ4ymupVuVFyTXqueOlfKTjXAoGOPsiLvuCfKfsFdqxEhcrJtgalGWHx1rAcvktxfYUs1Nm_b4SN2kH3an9xuzllkvUjY2XNWLykAgMOwVNMtPsQn9p6CY5IRO13ZX5-5AX-GfsF0VSjOIJT77tc9iv3XwdNPZuwmRRikPBfpUEw.r1_PqhlNOE7qBsyvxfweGY_jR6g47EEwZrQdWYQ4RyY&dib_tag=se&keywords=AUTOMATIC%2BTRASH%2Bcan&qid=1723668032&s=home-garden&sprefix=automatic%2Btrash%2Bca%2Cgarden%2C500&sr=1-4&th=1", headers=HEADERS)

amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
subprice = soup.find(name="span", class_="a-price-fraction").getText()
product = soup.find(id="productTitle").getText().strip()

totalPrice = float(f"{price}{subprice}")
print(totalPrice)

content = f"{product} is now ${totalPrice}. Find it here: {URL}"
print(content)
print(type(content))

if totalPrice < 59:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs="yaseenj96@gmail.com",
                            msg=f"Subject:New Amazon Price Drop!\n\n{content}".encode("utf-8"))

