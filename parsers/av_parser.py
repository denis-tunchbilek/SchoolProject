from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


class av_parser():
    def __init__(self, tovar):
        self.link = "https://av.ru/search/?text=" + tovar
        self.driver = webdriver.Chrome("./chromedriver")
    def pars(self):
        self.driver.get(self.link)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Москва')]").click()
        WebDriverWait(self.driver, timeout=10).until(presence_of_element_located((By.XPATH, ".//div[@class=\'product catalog-products_list_item\']")))
        self.page_source = self.driver.page_source
        self.soup = bs(self.page_source, "lxml")
        with open("test.html", 'w', encoding='utf-8') as file:
            file.write(self.page_source)
        for i in self.soup.find_all(attrs={'data-v-ac17228c class': 'product-info'}):
            print(i)
            self.name = i.find("a", class_="text product-info_name-container text--type-text text--font-inherit").text
            self.price = i.find("div", class_="price product-price_current-price").text
            print(self.name, self.price)

    def close(self):
        self.driver.close()
av = av_parser("мука")
print(av.pars())

