import requests
from bs4 import BeautifulSoup as bs




class magnit_parser():
    def __init__(self, tovar):
        self.link = "https://dostavka.magnit.ru/express/search?q=" + tovar
        ua = UserAgent()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': str(ua.chrome)
        }
        self.r = requests.get(self.link, headers)
        print(self.r.status_code)
        self.soup = bs(self.r.text, "lxml")
    def pars(self):
        for i in self.soup.find_all("a", class_="app-link product-card product-list__item"):
            self.name = i.find("span", class_="text__content").text
            self.price = i.find("div", class_="m-price__current").next.text
            return self.name, self.price

ma = magnit_parser("мука")
print(ma.pars())


