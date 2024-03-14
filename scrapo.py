import requests
from bs4 import BeautifulSoup

def mayo_clinic (url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_data = soup.get_text()
        return text_data
    else:
        print("Failed to retrieve website data. Status code:", response.status_code)
        return None

website_url = 'https://www.mayoclinic.org/diseases-conditions/hip-fracture/diagnosis-treatment/drc-20373472?p=1'
text_data = mayo_clinic(website_url)

if text_data:
    print(text_data)
