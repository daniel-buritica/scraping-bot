import time

from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from bots.colsubsidio.util.MapperColsubsidio import to_model


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    time.sleep(10)
    products = driver.find_elements(By.CSS_SELECTOR, "div.ImpreseeItem")

    for product in products:
        title = product.find_element(By.CSS_SELECTOR, "span.ImpreseeTitle").text
        price = product.find_element(By.CSS_SELECTOR, "span.ImpreseePrice").text
        img = product.find_element(By.CSS_SELECTOR, "img.ImpreseeItemImage")
        img_url = img.get_attribute("src")
        data = to_model(title, price, img_url)
        insert_db(data)

    driver.quit()


scraper("https://www.drogueriascolsubsidio.com/?IText=bloqueador")
