import time
from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from bots.localtel.util.MapperLocatel import to_model


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    products = driver.find_elements(By.CSS_SELECTOR, "section.vtex-product-summary-2-x-container")

    for product in products:
        title = product.find_element(By.CSS_SELECTOR, "span.vtex-product-summary-2-x-productBrand").text
        price = product.find_element(By.CSS_SELECTOR, "span.vtex-product-summary-2-x-currencyInteger").text + "000"
        img = product.find_element(By.CSS_SELECTOR, "img.vtex-product-summary-2-x-imageNormal")
        img_url = img.get_attribute("src")
        data = to_model(title, price, img_url)
        insert_db(data)

    driver.quit()


scraper("https://www.locatelcolombia.com/bloqueador?_q=bloqueador&map=ft")
