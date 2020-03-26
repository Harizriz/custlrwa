import urllib.request
import json
import re
import psycopg2

category_site = {
    'Women': 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?params=%7B%22url%22%3A%22%2Fwomen%2Fclothing%22%2C%22q%22%3A%22%22%2C%22sort%22%3A%22popularity%22%2C%22dir%22%3A%22desc%22%2C%22offset%22%3A{}%2C%22limit%22%3A{}%2C%22category_id%22%3A%5B%223%22%5D%2C%22range%22%3A%5B%5D%2C%22occasion%22%3A%5B%5D%2C%22material_composition%22%3A%5B%5D%2C%22pattern%22%3A%5B%5D%2C%22campaign_categoryId%22%3A%5B%5D%2C%22color%22%3A%5B%5D%2C%22sizesystem%22%3A%5B%5D%2C%22brand%22%3A%5B%5D%2C%22age_group%22%3A%5B%5D%2C%22gender%22%3A%5B%22women%22%5D%2C%22price%22%3A%22%22%2C%22normalized_sell_through%22%3A%22%22%2C%22segment%22%3A%22women%22%2C%22special_price%22%3Afalse%2C%22all_products%22%3Afalse%2C%22new_products%22%3Afalse%2C%22top_sellers%22%3Afalse%2C%22catalogtype%22%3A%22Main%22%2C%22campaign%22%3A%22%22%2C%22discount%22%3A%22%22%2C%22age%22%3A%22%22%2C%22mp%22%3A%22%22%2C%22or%22%3A%22%22%2C%22shipment_type%22%3A%22%22%2C%22exs%22%3A%22%22%2C%22lang%22%3A%22en%22%2C%22is_brunei%22%3Afalse%2C%22sort_formula%22%3A%22%22%2C%22rerank_formula%22%3A%22%22%2C%22search_suggest%22%3Afalse%2C%22custom_filters%22%3A%7B%22filter1%22%3A%22%22%2C%22filter2%22%3A%22%22%2C%22filter3%22%3A%22%22%2C%22filter4%22%3A%22%22%7D%2C%22elevate_ids%22%3A%5B%5D%2C%22user_id%22%3A%22%22%2C%22enable_visual_sort%22%3Atrue%2C%22enable_filter_ads%22%3Atrue%2C%22features%22%3A%7B%22compact_catalog_desktop%22%3Afalse%2C%22name_search%22%3Afalse%2C%22solr7_support%22%3Afalse%2C%22pick_for_you%22%3Afalse%2C%22learn_to_sort_catalog%22%3Afalse%7D%2C%22onsite_filters%22%3A%7B%7D%2C%22user_query%22%3A%22%22%7D',
    'Men': 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?params=%7B%22url%22%3A%22%2Fmen%2Fclothing%22%2C%22q%22%3A%22%22%2C%22sort%22%3A%22popularity%22%2C%22dir%22%3A%22desc%22%2C%22offset%22%3A{}%2C%22limit%22%3A{}%2C%22category_id%22%3A%5B%2226%22%5D%2C%22range%22%3A%5B%5D%2C%22occasion%22%3A%5B%5D%2C%22material_composition%22%3A%5B%5D%2C%22pattern%22%3A%5B%5D%2C%22campaign_categoryId%22%3A%5B%5D%2C%22color%22%3A%5B%5D%2C%22sizesystem%22%3A%5B%5D%2C%22brand%22%3A%5B%5D%2C%22age_group%22%3A%5B%5D%2C%22gender%22%3A%5B%22men%22%5D%2C%22price%22%3A%22%22%2C%22normalized_sell_through%22%3A%22%22%2C%22segment%22%3A%22men%22%2C%22special_price%22%3Afalse%2C%22all_products%22%3Afalse%2C%22new_products%22%3Afalse%2C%22top_sellers%22%3Afalse%2C%22catalogtype%22%3A%22Main%22%2C%22campaign%22%3A%22%22%2C%22discount%22%3A%22%22%2C%22age%22%3A%22%22%2C%22mp%22%3A%22%22%2C%22or%22%3A%22%22%2C%22shipment_type%22%3A%22%22%2C%22exs%22%3A%22%22%2C%22lang%22%3A%22en%22%2C%22is_brunei%22%3Afalse%2C%22sort_formula%22%3A%22%22%2C%22rerank_formula%22%3A%22%22%2C%22search_suggest%22%3Afalse%2C%22custom_filters%22%3A%7B%22filter1%22%3A%22%22%2C%22filter2%22%3A%22%22%2C%22filter3%22%3A%22%22%2C%22filter4%22%3A%22%22%7D%2C%22elevate_ids%22%3A%5B%5D%2C%22user_id%22%3A%22%22%2C%22enable_visual_sort%22%3Atrue%2C%22enable_filter_ads%22%3Atrue%2C%22features%22%3A%7B%22compact_catalog_desktop%22%3Afalse%2C%22name_search%22%3Afalse%2C%22solr7_support%22%3Afalse%2C%22pick_for_you%22%3Afalse%2C%22learn_to_sort_catalog%22%3Afalse%7D%2C%22onsite_filters%22%3A%7B%7D%2C%22user_query%22%3A%22%22%7D',
    'Kids': 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?params=%7B%22url%22%3A%22%2Fkids%2Fclothing%22%2C%22q%22%3A%22%22%2C%22sort%22%3A%22popularity%22%2C%22dir%22%3A%22desc%22%2C%22offset%22%3A{}%2C%22limit%22%3A{}%2C%22category_id%22%3A%5B%22557%22%5D%2C%22range%22%3A%5B%5D%2C%22occasion%22%3A%5B%5D%2C%22material_composition%22%3A%5B%5D%2C%22pattern%22%3A%5B%5D%2C%22campaign_categoryId%22%3A%5B%5D%2C%22color%22%3A%5B%5D%2C%22sizesystem%22%3A%5B%5D%2C%22brand%22%3A%5B%5D%2C%22age_group%22%3A%5B%5D%2C%22gender%22%3A%5B%5D%2C%22price%22%3A%22%22%2C%22normalized_sell_through%22%3A%22%22%2C%22segment%22%3A%22kids%22%2C%22special_price%22%3Afalse%2C%22all_products%22%3Afalse%2C%22new_products%22%3Afalse%2C%22top_sellers%22%3Afalse%2C%22catalogtype%22%3A%22Main%22%2C%22campaign%22%3A%22%22%2C%22discount%22%3A%22%22%2C%22age%22%3A%22%22%2C%22mp%22%3A%22%22%2C%22or%22%3A%22%22%2C%22shipment_type%22%3A%22%22%2C%22exs%22%3A%22%22%2C%22lang%22%3A%22en%22%2C%22is_brunei%22%3Afalse%2C%22sort_formula%22%3A%22%22%2C%22rerank_formula%22%3A%22%22%2C%22search_suggest%22%3Afalse%2C%22custom_filters%22%3A%7B%22filter1%22%3A%22%22%2C%22filter2%22%3A%22%22%2C%22filter3%22%3A%22%22%2C%22filter4%22%3A%22%22%7D%2C%22elevate_ids%22%3A%5B%5D%2C%22user_id%22%3A%22%22%2C%22enable_visual_sort%22%3Atrue%2C%22enable_filter_ads%22%3Atrue%2C%22features%22%3A%7B%22compact_catalog_desktop%22%3Afalse%2C%22name_search%22%3Afalse%2C%22solr7_support%22%3Afalse%2C%22pick_for_you%22%3Afalse%2C%22learn_to_sort_catalog%22%3Afalse%7D%2C%22onsite_filters%22%3A%7B%7D%2C%22user_query%22%3A%22%22%7D'
}
product_id = 1

connection = psycopg2.connect(host='localhost',
                              user='custlrwa',
                              password='YFlDM1lY6Uq1sRcd',
                              dbname='custlrwa')
cursor = connection.cursor()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

cursor.execute('DELETE FROM site_scraper_sizing;')
cursor.execute('DELETE FROM site_scraper_imageurl;')
cursor.execute('DELETE FROM site_scraper_scrapedresult;')
cursor.execute('ALTER SEQUENCE site_scraper_sizing_id_seq RESTART 1;')
cursor.execute('ALTER SEQUENCE site_scraper_imageurl_id_seq RESTART 1;')

for category, ZaloraSite in category_site.items():
    offset = 0
    limit = 400
    print(category)
    while True:
        try:
            jsonObj = json.loads(urllib.request.urlopen(urllib.request.Request(url=ZaloraSite.format(offset, limit), headers=headers)).read())
        except:
            break
        else:
            maxOffset = jsonObj['response']['numFound']
            # sql_count_size = 'SELECT COUNT(*) FROM `site_scraper_sizing` WHERE `description` = %s;'
            sql_insert_product = 'INSERT INTO site_scraper_scrapedresult (id, product_name, price, currency, brand, original_site, category, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            sql_insert_size = 'INSERT INTO site_scraper_sizing (sizing, product_id) VALUES (%s, %s);'
            sql_insert_image = 'INSERT INTO site_scraper_imageurl (image_url, product_id) VALUES (%s, %s);'

            for i in range(len(jsonObj['response']['docs'])):
                product_name = jsonObj['response']['docs'][i]['meta']['name']
                price = re.sub('[^\d\.]', '', jsonObj['response']['docs'][i]['meta']['price']) if not jsonObj['response']['docs'][i]['meta']['special_price'] else re.sub('[^\d\.]', '', jsonObj['response']['docs'][i]['meta']['special_price'])
                currency = re.sub('[\d\. ]', '', jsonObj['response']['docs'][i]['meta']['price']) if not jsonObj['response']['docs'][i]['meta']['special_price'] else re.sub('[\d\.NOW ]', '', jsonObj['response']['docs'][i]['meta']['special_price'])
                brand = jsonObj['response']['docs'][i]['meta']['brand']
                original_site = 'https://www.zalora.com.my/' + jsonObj['response']['docs'][i]['link']
                image_url = jsonObj['response']['docs'][i]['image']
                cursor.execute(sql_insert_product, (product_id, product_name, price, currency, brand, original_site, category, image_url))

                for size in jsonObj['response']['docs'][i]['available_sizes']:
                    cursor.execute(sql_insert_size, (size['size'].upper(), product_id))
                    # cursor.execute(sql_count_size, (size['size'].upper()))
                    # if (cursor.fetchone()[0] == 0):
                    #     cursor.execute(sql_insert_size, (size['size'].upper(), size['size'].upper()))

                cursor.execute(sql_insert_image, (jsonObj['response']['docs'][i]['image'], product_id))
                for img in jsonObj['response']['docs'][i]['image_extra']:
                    cursor.execute(sql_insert_image,(img['url'], product_id))

                product_id += 1
                # print(cursor._last_executed)

            offset += 400
            print(str(offset) + ' results inserted')
            if (offset + 400) > maxOffset:
                break
    print()

connection.commit()