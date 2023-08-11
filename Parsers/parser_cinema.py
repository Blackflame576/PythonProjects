import requests
from bs4 import BeautifulSoup
import time

url = 'https://market.yandex.ru/product--tverdotelnyi-nakopitel-western-digital-wd-blue-sata-500-gb-wds500g2b0b/1914879533/offers?how=aprice&grhow=supplier&sku=1914879533&cpa=0&qrfrom=4&onstock=1&local-offers-first=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='_3NaXxl-HYN _3Um__wpmuT _1cFflWx7Th')

for quote in quotes:
    print('\n' +  quote.text)


