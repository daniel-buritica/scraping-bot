from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bots.cruzverde.util.MapperCruzVerde import to_model

import time


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Aceptar')]")
    for button in buttons:
        button.click()
        break

    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, "ml-card-product.ng-star-inserted")

    for product in products:
        title = product.find_element(By.CSS_SELECTOR, "span.ng-star-inserted").text
        price = product.find_element(By.CSS_SELECTOR, "span.text-prices").text

        try:
            img = product.find_element(By.CSS_SELECTOR, "img.lazyloaded")
            img_url = img.get_attribute("src")
        except Exception as e:
            img_url = "https://beta1.cruzverde.com.co/dw/image/v2/BDPM_PRD/on/demandware.static/-/Sites-masterCatalog_Colombia/default/dwddb9af99/images/large/80323_1_SUNFACE_GEL_TUB_X_70GR_SPF_50_.jpg?sw=295&sh=295"
        data = to_model(title, price, img_url)
        insert_db(data)

    driver.quit()


scraper("https://www.cruzverde.com.co/search?query=bloqueadores")
