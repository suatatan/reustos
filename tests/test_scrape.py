import unittest
import os 
import sys
# Get the absolute path of the parent directory (project root)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to the Python path
sys.path.insert(0, parent_dir)
from src.scrape import SinglePageScraper

class TestSinglePageScraper(unittest.TestCase):
    def test_scrape(self):
        # Test scraping functionality
        url = 'https://www.walmart.com/reviews/product/797596359'  # Replace with the actual URL you want to scrape
        brand = 'Samsung'
        product_name = 'Samsung Galaxy Watch4 Classic Smartwatch, 42mm, Bluetooth, Black'
        scraper = SinglePageScraper(url, brand, product_name)
        scraped_data = scraper.scrape()
        print(scraped_data)
        self.assertIsNotNone(scraped_data)
        # Add assertions to check if scraping and database insertion worked as expected

if __name__ == '__main__':
    unittest.main()
