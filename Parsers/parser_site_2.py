import requests
from bs4 import BeautifulSoup
import time

url = 'https://anysoftware64.herokuapp.com/'
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('p', class_='lead1')

    for quote in quotes:
        print('\n' +  quote.text)