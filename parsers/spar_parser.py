from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


class spar_parser():
    def __init__(self, tovar):
        self.link = "https://myspar.ru/#search?query=" + tovar
        self.driver = webdriver.Chrome("./chromedriver")
    def pars(self):
        self.driver.get(self.link)
        WebDriverWait(self.driver, timeout=10).until(presence_of_element_located((By.XPATH, ".//div[@class=\'smartsearch__product-info\']")))
        self.page_source = self.driver.page_source
        self.soup = bs(self.page_source, "lxml")
        for i in self.soup.find_all("div", class_="smartsearch__product-info"):
            self.name = i.find("a", class_="smartsearch__product-name").text
            self.price = i.find("div", class_="smartsearch__product-price").text
            return self.name, self.price
    def close(self):
        self.driver.close()
        
s = spar_parser("мука")
print(s.pars())