import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json
import sys 
import os



class WebScrapping:
    def __init__(self):
        value = sys.argv[1]

        page = requests.get(
            f'https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q={value}&btnG='
        )

        soup = BeautifulSoup(page.content, 'html.parser')
        
        result = self.filter_div(soup)
        links = self.get_links(result)
        
        
        
        result_json = self.create_json(links[2])
        
        print(str(result_json))

        #self.driver_firefox(result_json)
        
        
    def filter_div(self, soup):
        result = soup.find(id='gs_bdy')
        result = result.find(id='gs_bdy_ccl')
        return result



    def get_links( self, objSoup):
        links = []
        for link in objSoup.find_all('a'):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in link:
                    links.append(link.attrs['href'])
        return links


    def create_json(self, soup_link):
        # Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
        with open('result.json', 'w', encoding='utf-8') as jp:
            js = json.dumps(soup_link, indent=4)
            jp.write(js)
            return js



    def driver_firefox( self, url):

        path_driver = webdriver.Firefox(executable_path 
            = r'geckodriver.exe')

        option = Options()
        option.headless = True
        driver = webdriver.Firefox( options=option, executable_path=path_driver)
        driver.get('http://inventwithpython.com')
        driver.get(url)
        driver.implicitly_wait(10)  # in seconds
        driver.close()


if __name__ == "__main__":
    WebScrapping()