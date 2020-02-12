from requests import get
from bs4 import BeautifulSoup

URL = 'https://www.zalora.com.my/women/clothing/'
response = get(URL)

# soup = BeautifulSoup(response.content, 'html5lib')
# print(response.content)

