from selenium import webdriver
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