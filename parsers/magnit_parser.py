import requests
from bs4 import BeautifulSoup as bs


class magnit_parser():
    def __init__(self, tovar):
        self.link = "https://dostavka.magnit.ru/express/search?q=" + tovar
        self.r = requests.get(self.link)
        self.soup = bs(self.r.text, "lxml")
    def pars(self):
        for i in self.soup.find_all("a", class_="app-link product-card product-list__item"):
            self.name = i.find("span", class_="text__content").text
            self.price = i.find("div", class_="m-price__current").next.text
            return self.name, self.price

ma = magnit_parser("мука")
print(ma.pars())


