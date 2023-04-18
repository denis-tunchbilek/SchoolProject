from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By





class perik_pars():
  def __init__(self, product):
    self.product = product
    self.link = "https://www.perekrestok.ru/cat/search?search=" + self.product
    self.driver = webdriver.Chrome("./chromedriver")
  def pars(self):
      self.driver.get(self.link)
      WebDriverWait(self.driver, timeout=10).until(presence_of_element_located((By.XPATH, ".//div[@class=\'product-card-wrapper\']")))
      self.page_source = self.driver.page_source
      self.soup = bs(self.page_source, "lxml")
      for i in self.soup.find_all("div", class_="product-card-wrapper"):
        self.name = i.find("span", class_="product-card__link-text").text
        self.rating = i.find("div", class_="rating-value").text
        self.price = i.find("div", class_="price-new").text
        return self.name, self.price
  def close(self):
    self.driver.close()

muka = perik_pars("кокос")
print(muka.pars())
muka.close()
