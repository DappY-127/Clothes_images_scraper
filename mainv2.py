from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
from urllib.parse import urlparse


class ReservedProductPageLocators():
    clothes_name_locator = '[data-selen="product-name"]'
    clothes_price_locator = '.basic-pricestyled__StyledBasicPrice-ptbrpf-0'
    clothes_id_locator = '[data-selen="sku"]'
    clothes_pic_locator = '.thumbnail__Thumbnail-cghdsl-0 img' 

class HouseProductPageLocators():
    clothes_name_locator = '[data-testid="product-name"]'
    clothes_price_locator = '[data-selen="product-price"]'
    clothes_id_locator = '[data-testid="sku"]'
    clothes_pic_locator = '.thumbnailstyled__Thumbnail-sc-4pvlpr-0 img'

class SinsayProductPageLocators():
    clothes_name_locator = 'h1[data-selen="product-name"]'
    clothes_price_locator = '[data-selen="product-price"].basic-price'
    clothes_id_locator = '[data-selen="sku"]'
    clothes_pic_locator = '.thumbnail__Thumbnail-cghdsl-0 img'   

class CroppProductPageLocators():
    clothes_name_locator = '[data-selen="product-name"]'
    clothes_price_locator = '[data-selen="product-price"]'
    clothes_id_locator = '[data-selen="sku"]'
    clothes_pic_locator = '.thumbnail__Thumbnail-cghdsl-0 img'  

class MohitoProductPageLocators():
    clothes_name_locator = '[data-testid="product-name"]'
    clothes_price_locator = '.desktop__PriceWrapper-mr1wyi-3' # might be incorect
    clothes_id_locator = '[data-testid="sku"]'
    clothes_pic_locator = '.thumbnailstyled__Thumbnail-sc-12kuo2j-0 img' 

LOCATORS = {
    'reserved': ReservedProductPageLocators,
    'house': HouseProductPageLocators,
    'sinsay': SinsayProductPageLocators,
    'cropp': CroppProductPageLocators,
    'mohito': MohitoProductPageLocators,
}

def prepare_link(links):
    source_links = []
    for link in links:
        split_link = link.split('/')
        remove_part = [split_link[6], split_link[7], split_link[8]] # look at correct indexes
        for part in remove_part:
            split_link.remove(part)
        source_link = '/'.join(split_link)
        source_links.append(source_link)
    return source_links 

def download_images(directory, image_links, image_names):
    counter = 0
    for link in image_links:
        save_as = os.path.join(directory, f'{image_names[counter]}.jpg')
        wget.download(link, save_as)
        counter += 1

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

        # Determine the corresponding locator class based on the domain of the URL
        domain = urlparse(self.url).hostname
        if 'reserved.com' in domain:
            locator_class = ReservedProductPageLocators
        elif 'house.com' in domain:
            locator_class = HouseProductPageLocators
        elif 'sinsay.com' in domain:
            locator_class = SinsayProductPageLocators
        elif 'cropp.com' in domain:
            locator_class = CroppProductPageLocators
        elif 'mohito.com' in domain:
            locator_class = MohitoProductPageLocators
        else:
            raise ValueError(f"No locator class found for domain '{domain}'")

        # Extract data using the locators from the corresponding locator class
        name_locator = getattr(locator_class, 'clothes_name_locator')
        price_locator = getattr(locator_class, 'clothes_price_locator')
        id_locator = getattr(locator_class, 'clothes_id_locator')
        pic_locator = getattr(locator_class, 'clothes_pic_locator')

        name = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, name_locator))).text
        price = driver_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, price_locator)))
        item_id = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, id_locator))).text
        clothes_pics = driver.find_elements(By.CSS_SELECTOR, pic_locator)
        image_links = [clothes.get_attribute('src') for clothes in clothes_pics]
        image_names = [clothes.get_attribute('alt') for clothes in clothes_pics]
        image_links = prepare_link(image_links)

        driver.quit()
        
        self.name = name
        self.price = price
        self.id = item_id
        self.image_links = image_links
        self.image_names = image_names

    def create_directory(self):
        path = os.getcwd()
        domain = urlparse(self.url).hostname
        if 'reserved.com' in domain:
            folder_name = 'Reserved'
        elif 'house.com' in domain:
            folder_name = 'House'
        elif 'sinsay.com' in domain:
            folder_name = 'Sinsay'
        elif 'cropp.com' in domain:
            folder_name = 'Cropp'
        elif 'mohito.com' in domain:
            folder_name = 'Mohito'
        else:
            raise ValueError(f"No folder found for domain '{domain}'")
        self.directory = os.path.join(path, f'images/{folder_name}/{self.name}({self.id})')
        os.makedirs(self.directory)

    def download_images(self):
        download_images(self.directory, self.image_links, self.image_names)
        
if __name__ == '__main__':
    urls = input("Enter the URLs separated by commas: ").split(",")
    for url in urls:
        item = ClothingItem(url.strip())
        item.extract_data()
        item.create_directory()
        item.download_images()              
