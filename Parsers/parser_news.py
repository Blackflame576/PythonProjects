import requests
from bs4 import BeautifulSoup
import time

url = 'https://riavrn.ru/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('h4', class_='heading')

for quote in quotes:
    print('\n' +  quote.text)