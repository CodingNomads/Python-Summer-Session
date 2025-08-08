import requests

from bs4 import BeautifulSoup

URL = "https://example.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text)

title = soup.find("title")
print(title.text)
