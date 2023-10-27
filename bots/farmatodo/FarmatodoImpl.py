from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from bots.farmatodo.util.MapperFarmaTodo import to_model


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    products = driver.find_elements(By.CSS_SELECTOR, "div.card-unique")

    for product in products:
        title = product.find_element(By.CSS_SELECTOR, "p.text-title").text
        price = product.find_element(By.CSS_SELECTOR, "span.text-price").text
        img = product.find_element(By.CSS_SELECTOR, "img.image")
        img_url = img.get_attribute("src")
        data = to_model(title, price, img_url)
        insert_db(data)
        print(1)

    driver.quit()



scraper("https://www.farmatodo.com.co/mundo-ofertas/49092")

