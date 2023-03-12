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
