import requests
from bs4 import BeautifulSoup

def extract_website_text(url):

    try:

        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text,'html.parser')

        for script in soup(["script","style"]):
            script.extract()

        text = soup.get_text()

        return " ".join(text.split())

    except:

        return "Website extraction failed"