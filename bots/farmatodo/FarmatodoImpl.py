# from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    products = driver.find_elements(By.CSS_SELECTOR, "div.card-unique")

    for producto in products:
        #title = producto.find_element(By.CSS_SELECTOR, "p.text-title").text
        #price = producto.find_element(By.CSS_SELECTOR, "span.text-price").text

        img = producto.find_element(By.CSS_SELECTOR, "img.image-virtual")
        print(img.get_attribute("class"))
        #print(title)
        #print(price)
        #print(img)

    driver.quit()

scraper("https://www.farmatodo.com.co/mundo-ofertas/49092")

