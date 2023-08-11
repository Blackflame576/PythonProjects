import requests
from bs4 import BeautifulSoup
import time

url = 'https://weblific.herokuapp.com/'
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('p', class_='lead')

    for quote in quotes:
        print('\n' +  quote.text)