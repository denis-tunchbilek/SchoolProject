from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By





class vv_pars():
  def __init__(self, product):
    self.product = product
    self.link = f"https://vkusvill.ru/search/?q={self.product}=products"
    self.driver = webdriver.Chrome("./chromedriver")
  def pars(self):
      self.driver.get(self.link)
      WebDriverWait(self.driver, timeout=10).until(presence_of_element_located((By.XPATH, ".//div[@class=\'ProductCard__content\']")))
      self.page_source = self.driver.page_source
      self.soup = bs(self.page_source, "lxml")
      for i in self.soup.find_all("div", class_="ProductCard__content"):
        self.name = i.find("a", class_="ProductCard__link rtext _desktop-md _mobile-sm gray900 js-datalayer-catalog-list-name").text
        self.price = i.find("span", class_="js-datalayer-catalog-list-price hidden").text
        return self.name, self.price
  def close(self):
    self.driver.close()

muka = vv_pars("кокос")
print(muka.pars())
muka.close()