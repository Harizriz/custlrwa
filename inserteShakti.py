import urllib.request
import json
import psycopg2
from requests import get
from bs4 import BeautifulSoup

category_site = {
    'Dresses': 'https://www.eshakti.com/Handler/ProductHandlerNew6.ashx?cate=Dresses&startIndex={}&endIndex={}&viewAll=&price=&color=&fabric=&sorting=Topsellers&feature=&userid=446454949&isNaturalFabric=false&promotion=&customerType=N',
    'Tops': 'https://www.eshakti.com/Handler/ProductHandlerNew6.ashx?cate=Tops&startIndex={}&endIndex={}&viewAll=&price=&color=&fabric=&sorting=Topsellers&feature=&userid=446454949&isNaturalFabric=false&promotion=&customerType=N',
    'Bottoms': 'https://www.eshakti.com/Handler/ProductHandlerNew6.ashx?cate=Bottoms&startIndex={}&endIndex={}&viewAll=&price=&color=&fabric=&sorting=Topsellers&feature=&userid=446454949&isNaturalFabric=false&promotion=&customerType=N'
}

connection = psycopg2.connect(host='localhost',
                              user='custlrwa',
                              password='YFlDM1lY6Uq1sRcd',
                              dbname='custlrwa')
cursor = connection.cursor()

cursor.execute('SELECT MAX(id) FROM site_scraper_scrapedresult;')
max_id = cursor.fetchone()[0]
product_id = 1 if max_id == None else max_id + 1

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

for category, eShaktiSite in category_site.items():
    start = 0
    end = 400
    print(category)
    while True:
        try:
            jsonObj = json.loads(urllib.request.urlopen(urllib.request.Request(url=eShaktiSite.format(start, end), headers=headers)).read())
        except:
            break
        else:
            maxOffset = jsonObj['Count']
            sql_insert_product = 'INSERT INTO site_scraper_scrapedresult (id, product_name, price, currency, brand, original_site, category, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            sql_insert_image = 'INSERT INTO site_scraper_imageurl (image_url, product_id) VALUES (%s, %s);'

            for i in range(len(jsonObj['product'])):
                product_name = jsonObj['product'][i]['Name']
                price = jsonObj['product'][i]['listprice']
                currency = 'USD'
                brand = jsonObj['product'][i]['isZapelle']
                original_site = 'https://www.eshakti.com/product/' + jsonObj['product'][i]['Productid']

                soup = BeautifulSoup(get(original_site, headers=headers).content, 'html5lib')
                try:
                    image_url = soup.select('#ContentPlaceHolder1_divthumbImgs #Img1')[0]['src']
                except:
                    try:
                        image_url = soup.select('#ContentPlaceHolder1_divthumbImgs')[0].find_all('a')[0]['href']
                    except:
                        image_url = ''

                cursor.execute(sql_insert_product, (product_id, product_name, price, currency, brand, original_site, 'Women', image_url))
                connection.commit()

                if soup.select('#ContentPlaceHolder1_divthumbImgs .myimage'):
                    for img in soup.select('#ContentPlaceHolder1_divthumbImgs .myimage'):
                        cursor.execute(sql_insert_image,(img['src'], product_id))
                        connection.commit()
                else:
                    for img in soup.select('#ContentPlaceHolder1_divthumbImgs')[0].find_all('a'):
                        cursor.execute(sql_insert_image,(img['href'], product_id))
                        connection.commit()

                product_id += 1
                print(str(i) + ' ' + product_name)
                # print(cursor._last_executed)

            start = end + 1
            end += 400
            if (end - 400) > maxOffset:
                print(str(maxOffset) + ' results inserted')
                break
            else:
                print(str(start - 1) + ' results inserted')
    print()

connection.commit()
