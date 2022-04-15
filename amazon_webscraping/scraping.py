import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_url(search_term):
    template = "https://www.amazon.com.br/s?k={}"
    search_term = search_term.replace(' ', '+')

    url = template.format(search_term)

    url += '&page{}'
    return url

def extract_record(item):
    atag = item.h2.a
    description  = atag.text.strip()
    url = 'https://www.amazon.com.br' + atag.get('href')


    try: 
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text

    except AttributeError:
        return 

    try:
        rating = item.i.text
        review_count = item.find('span', 'a-size-base s-underline-text').text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url)

    return result

def main(search_term):
    driver = webdriver.Chrome(ChromeDriverManager().install())


    record = []
    url = get_url(search_term)

    for page in (1, 8):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    driver.close()

    with open('results.csv', 'w', newline= '', encoding= 'utf-8' ) as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
        writer.writerows(records)

main('data science')

