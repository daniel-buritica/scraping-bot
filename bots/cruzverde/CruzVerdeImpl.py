from config.database.RepositoryDB import insert_db
from config.scrapper.ConfigWebDriverScrapper import setting_options_argument
from selenium.webdriver.common.by import By
from bots.farmatodo.util.MapperFarmaTodo import to_model


def scraper(url):
    driver = setting_options_argument()
    driver.get(url)
    buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Aceptar')]")
    for button in buttons:
        button.click()
        break












    driver.quit()



scraper("https://www.cruzverde.com.co/search?query=bloqueadores")
