import requests
from bs4 import BeautifulSoup as bs
import sys
import logging
import os


tovar = "мука"






URL_TEMPLATE = "https://www.perekrestok.ru/cat/search?search=мука"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "lxml")
with open('test.html', 'w', encoding="utf-8") as output_file:
  output_file.write(r.text)
product_cards = soup.find_all('a', class_="sc-dQoVA fvoiIk product-card__link")
print(product_cards)
