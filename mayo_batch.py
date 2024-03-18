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
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                text_data = mayo_batch(url)
                if text_data:
                    filename = url.split('/')[-1].split('.')[0] + '.json'
                    with open(filename, 'w') as json_file:
                        json.dump({'corpus': text_data}, json_file, indent=4)
                else:
                    print("No scraping done for", url)
    except FileNotFoundError:
        print("File not found:", file_path)

# Example: how it should be run; provide a .txt file with all the URLs that should be scraped 
file_path = 'link.txt'
scrape_file(file_path)
