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

site_folder_mapping = {
    'reserved': 'Reserved',
    'house': 'House',
    'sinsay': 'Sinsay',
    'cropp': 'Cropp',
    'mohito': 'Mohito'
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
