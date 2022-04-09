# Amazon webscraper

import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.amazon.com.br'
driver.get(url)

def get_url(search_term):
    template = "https://www.amazon.com.br/s?k={}&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=20TN7QFIX2IWC&sprefix={}}%2Caps%2C223&ref=nb_sb_noss_2"
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = get_url('data science')
print(url)