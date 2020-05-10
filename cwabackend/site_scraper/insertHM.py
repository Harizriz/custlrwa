"""
Inserts data from H&M
Done by Brandon
"""

import urllib.request
import json
import re
import psycopg2
from requests import get
from bs4 import BeautifulSoup
import js2py

category_site = {
    'Women': 'https://www2.hm.com/en_asia4/ladies/shop-by-product/view-all/_jcr_content/main/productlisting_30ab.display.json?offset={}&page-size={}',
    'Men': 'https://www2.hm.com/en_asia4/men/shop-by-product/view-all/_jcr_content/main/productlisting_fa5b.display.json?offset={}&page-size={}'
}

connection = psycopg2.connect(host='localhost',
                              user='custlrwa',
                              password='YFlDM1lY6Uq1sRcd',
                              dbname='custlrwa')
cursor = connection.cursor()

cursor.execute('SELECT id FROM site_scraper_scrapedresult ORDER BY id DESC LIMIT 1')
max_id = cursor.fetchone()[0]
if max_id == None:
    max_id = 1
else:
    max_id += 1

print(max_id)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

for category, HMSite in category_site.items():
    offset = 0
    pageSize = 100
    print(category)
    while True:
        try:
            jsonObj = json.loads(urllib.request.urlopen(urllib.request.Request(url=HMSite.format(offset, pageSize), headers=headers)).read())
        except:
            break
        else:
            maxOffset = jsonObj['total']
            sql_insert_product = 'INSERT INTO site_scraper_scrapedresult (id, product_name, price, currency, brand, original_site, category, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            sql_insert_size = 'INSERT INTO site_scraper_sizing (sizing, product_id) VALUES (%s, %s);'
            sql_insert_image = 'INSERT INTO site_scraper_imageurl (image_url, product_id) VALUES (%s, %s);'

            for i in range(len(jsonObj['products'])):
                product_name = jsonObj['products'][i]['title']
                price = re.sub('[^\d\.]', '', jsonObj['products'][i]['price'])
                currency = re.sub('[\d\. ]', '', jsonObj['products'][i]['price'])
                original_site = 'https://www2.hm.com' + jsonObj['products'][i]['link']

                soup = BeautifulSoup(get(original_site, headers=headers).content, 'html5lib')
                productArticleDetails = js2py.eval_js('var isDesktop = true;' + re.search('var productArticleDetails = ([\s\S]*);', str(soup.select('.product.parbase script')[0])).group(0))
                image_url = 'https:' + productArticleDetails[jsonObj['products'][i]['articleCode']]['images'][0]['zoom']

                cursor.execute(sql_insert_product, (max_id, product_name, price, currency, 'H&M', original_site, category, image_url))
                connection.commit()

                for img in productArticleDetails[jsonObj['products'][i]['articleCode']]['images']:
                    cursor.execute(sql_insert_image,('https:' + img['zoom'], max_id))
                    connection.commit()

                availability = json.loads(urllib.request.urlopen(urllib.request.Request(url='https://www2.hm.com/hmwebservices/service/product/asia4/availability/{}.json'.format(jsonObj['products'][i]['articleCode'][0:7]), headers=headers)).read())['availability']
                for size in productArticleDetails[jsonObj['products'][i]['articleCode']]['sizes']:
                    if any(size['sizeCode'] in code for code in availability):
                        cursor.execute(sql_insert_size, (size['name'], max_id))
                        connection.commit()

                max_id += 1
                print(str(i) + ' ' + product_name)
                # print(cursor._last_executed)

            offset += pageSize
            if offset >= maxOffset:
                print(str(maxOffset) + ' results inserted')
                break
            else:
                print(str(jsonObj['itemsShown']) + ' results inserted')
    print()

connection.commit()