import requests
from bs4 import BeautifulSoup
import json

def mayo_batch(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_data = soup.get_text()
        return text_data
    else:
        return None

def scrape_file(file_path):
    scraped_data = {}
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                text_data = mayo_batch(url)
                if text_data:
                    scraped_data[url] = text_data
                else:
                    print("No scrapping done", url)
    except FileNotFoundError:
        print("File not found:", file_path)
    
    with open('mayo_saved.json', 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)

# example: how it should be run; provide a .txt file with all the urls that should be scrapped 
# file_path = 'urls.txt'
# scrape_file(file_path)
