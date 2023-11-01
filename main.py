import requests
import bs4

headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  "Accept-Language": 'en-US,en;q=0.9'
}
response = requests.get('https://www.amazon.com/LEXiBOOK-Miraculous-Educational-Bilingual-Activities/dp/B0B6HKB3JF/ref=sr_1_1_sspa?crid=3II92RG1YA1N6&keywords=baby%2Blaptop&qid=1699846232&sprefix=baby%2Blaptop%2Caps%2C121&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1', headers=headers)

print(response.text)