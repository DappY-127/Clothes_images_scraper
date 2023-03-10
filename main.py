from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

class ClothingItem:
    def __init__(self, url):
        self.url = url
        self.name = None
        self.price = None
        self.id = None
        self.image_links = []
        self.image_names = []
        self.directory = None

    def extract_data(self):
        driver = webdriver.Chrome(executable_path='drivers\chromedriver.exe')
        driver.maximize_window()
        driver.get(self.url)
        driver_wait = WebDriverWait(driver, 10)

        clothes_name_locator = '[data-selen="product-name"]'
        clothes_price_locator = '.basic-pricestyled__StyledBasicPrice-ptbrpf-0'
        clothes_id_locator = '[data-selen="sku"]'
        clothes_pic_locator = '.thumbnail__Thumbnail-cghdsl-0 img'

        self.name = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, clothes_name_locator))).text
        self.price = driver_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, clothes_price_locator)))
        self.id = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, clothes_id_locator))).text
        clothes_pics = driver.find_elements(By.CSS_SELECTOR, clothes_pic_locator)
        self.image_links = [clothes.get_attribute('src') for clothes in clothes_pics]
        self.image_names = [clothes.get_attribute('alt') for clothes in clothes_pics]
        self.image_links = self.prepare_link(self.image_links)    

    def create_directory(self):
        path = os.getcwd()
        self.directory = os.path.join(path, f'Reserved\ClothesV2\{self.name}({self.id})')
        os.mkdir(self.directory)  

    def download_images(self):
        counter = 0
        for link in self.image_links:
            save_as = os.path.join(self.directory, f'{self.image_names[counter]}.jpg')
            wget.download(link, save_as)
            counter += 1    

if __name__ == '__main__':
    url = 'plug'    
    item = ClothingItem(url)   
    item.extract_data()
    item.create_directory()
    item.download_images()
 