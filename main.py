import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 40
headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  "Accept-Language": 'en-US,en;q=0.9'
}
url = 'https://www.amazon.com/LEXiBOOK-Miraculous-Educational-Bilingual-Activities/dp/B0B6HKB3JF/ref=sr_1_1_sspa?crid=3II92RG1YA1N6&keywords=baby%2Blaptop&qid=1699846232&sprefix=baby%2Blaptop%2Caps%2C121&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

def get_price():

  response = requests.get('https://www.amazon.com/LEXiBOOK-Miraculous-Educational-Bilingual-Activities/dp/B0B6HKB3JF/ref=sr_1_1_sspa?crid=3II92RG1YA1N6&keywords=baby%2Blaptop&qid=1699846232&sprefix=baby%2Blaptop%2Caps%2C121&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1', headers=headers)

  soup = BeautifulSoup(response.content, 'lxml')

  price = soup.find(class_="a-offscreen")
  title = soup.find(id="productTitle")
  try:
    return price.get_text()
  except AttributeError:
    return None

price = get_price()

while price is None:
  price = get_price()

price_without_currency = price.split('$')[1]
price_as_float = float(price_without_currency)
print(price_as_float)


if price_as_float < BUY_PRICE:
  message = f'The kids laptop is now {price}'
  with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    result = connection.login('alonzosanchez3@gmail.com', 'knui yyfd mqlt igcb')
    connection.sendmail(from_addr='alonzosanchez3@gmail.com', to_addrs='alonzosanchez3@gmail.com', msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8'))
