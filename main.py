from selenium import webdriver
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

if __name__ == '__main__':
    url = 'plug'    
    item = ClothingItem(url)    