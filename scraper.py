from requests import get
from bs4 import BeautifulSoup

UniqloSite = 'https://www.uniqlo.com/my/store/specommerce/ajax/category/?cid=892&pid=319&ajax=1&mode=grid'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

response = get(UniqloSite, headers=headers)

soup = BeautifulSoup(response.content, 'html5lib')

Items = []

for row in soup.select('li.item'):
    Item = {}
    Item['product_name'] = row.find('h2', class_ = 'product-name').a.text
    Item['price'] = row.find('span', id = 'product-price').text
    Item['url'] = row.find('h2', class_ = 'product-name').a['href']
    Item['image_url'] = 'https:' + row.find('img', class_ = 'lazy')['data-original']
    DataModelCodeValue = row.find('span', class_ = 'quickView')['data-modelcodevalue']
    Item['available_sizes'] = []
    for size in row.find('div', class_ = 'sizechip-wrapper').find_all('li'): # need to use DataModelCodeValue here
        if 'sizeoos' not in size['class']:
            Item['available_sizes'].append(size['size'])
    Item['more_details'] = 'https://uqmy-media.s3.amazonaws.com/json/' + DataModelCodeValue + '.json'
    Items.append(Item)

print(Items)

# print(Table_ul[1])