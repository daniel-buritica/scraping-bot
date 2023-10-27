from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from bots.farmatodo.util.MapperFarmaTodo import to_model
import time


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Aceptar')]")
    for button in buttons:
        button.click()
        time.sleep(3)
        break
    products = driver.find_elements(By.CSS_SELECTOR, "ml-card-product.ng-star-inserted")

    for product in products:
        title = product.find_element(By.CSS_SELECTOR, "span.ng-star-inserted").text
        price = product.find_element(By.CSS_SELECTOR, "span.text-prices").text
        try:
        img = product.find_element(By.CSS_SELECTOR, "img.lazyloaded")
        img_url = img.get_attribute("src")

        print(title)
        print(price)
        print(img_url)


    driver.quit()


scraper("https://www.cruzverde.com.co/search?query=bloqueadores")
