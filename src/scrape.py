import os
import peewee as pw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from fake_useragent import UserAgent

db = pw.SqliteDatabase('reustos.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class ScrapedData(BaseModel):
    url = pw.CharField()
    brand = pw.CharField()
    product_name = pw.CharField()
    date = pw.DateTimeField()
    data = pw.TextField()

class Works(BaseModel):
    url = pw.CharField()
    brand = pw.CharField()
    product_name = pw.CharField()
    date = pw.DateTimeField()
    scraped_data_amount = pw.IntegerField()

class SinglePageScraper:
    def __init__(self, url, brand, product_name):
        self.url = url
        self.brand = brand
        self.product_name = product_name
        db.connect()
        db.create_tables([ScrapedData, Works])

    def scrape(self):
        existing_data = ScrapedData.select().where(ScrapedData.url == self.url, ScrapedData.brand == self.brand).first()
        if existing_data:
            print(f"Data already scraped for this brand and URL. {self.brand} {self.product_name}")
            return "Already Scraped"

        user_agent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={user_agent}")
        driver = webdriver.Chrome(options)

        driver.get(self.url)

        scraped_data = driver.page_source

        current_date = datetime.datetime.now()

        new_scraped_data = ScrapedData.create(
            url=self.url,
            brand=self.brand,
            product_name=self.product_name,
            date=current_date,
            data=scraped_data
        )

        new_work = Works.create(
            url=self.url,
            brand=self.brand,
            product_name=self.product_name,
            date=current_date,
            scraped_data_amount=len(scraped_data)
        )

        driver.quit()
        return scraped_data

# if __name__ == '__main__':
#     url = 'https://www.walmart.com/reviews/product/797596359'  # Replace with the actual URL you want to scrape
#     brand = 'Samsung'
#     product_name = 'Samsung Galaxy Watch4 Classic Smartwatch, 42mm, Bluetooth, Black'

#     scraper = SinglePageScraper(url, brand, product_name)
#     scraper.scrape()
