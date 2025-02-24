import requests
from bs4 import BeautifulSoup

def extractLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = [a["href"] for a in soup.find_all('a')]
    return links
    


url = "https://www.iana.org/help/example-domains"
print(extractLinks(url))