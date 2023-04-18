from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By

class metro_parser():
    def __init__(self, tovar):
        self.link = "https://online.metro-cc.ru/search?q=" + tovar
        self.driver = webdriver.Chrome("./chromedriver")
    def pars(self):
        self.driver.get(self.link)
        WebDriverWait(self.driver, timeout=10).until(presence_of_element_located((By.XPATH, ".//div[@class=\'product-card__content\']")))
        self.page_source = self.driver.page_source
        self.soup = bs(self.page_source, "lxml")
        for i in self.soup.find_all("div", class_="product-card__content"):
            self.name = i.find("span", class_="product-card-name__text").text
            self.price = i.find("span", class_="product-price__sum-rubles").text
            return self.name, self.price
    def close(self):
        self.driver.close()

m = metro_parser("кокос")
print(m.pars())