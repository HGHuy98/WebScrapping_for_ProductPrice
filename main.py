
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



def main():
    driver = webdriver.Chrome()
    driver.get('https://riderdepot.com.vn/')

    result_table = []
    
    content = driver.page_source
    ScrappedWeb = BeautifulSoup(content, 'html.parser')

    for element in ScrappedWeb.find_all(attrs={'class': 'product-info'}):
        product_name = element.find('a')
        
        if product_name not in result_table:
            result_table.append(product_name.text)


    for product_name in result_table:
        print(product_name)



if __name__ == "__main__":
    main()