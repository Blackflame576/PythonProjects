import requests
from bs4 import BeautifulSoup
import time

url = 'https://market.yandex.ru/product--operativnaia-pamiat-patriot-memory-sl-16gb-2400mhz-cl17-psd416g24002s/1976634020/offers?cpa=0&how=aprice&grhow=supplier&onstock=1&local-offers-first=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='_3NaXxl-HYN _3Um__wpmuT _1cFflWx7Th')

for quote in quotes:
    print('\n' +  quote.text)