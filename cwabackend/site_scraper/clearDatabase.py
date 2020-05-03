import psycopg2

connection = psycopg2.connect(host='localhost',
                              user='custlrwa',
                              password='YFlDM1lY6Uq1sRcd',
                              dbname='custlrwa')
cursor = connection.cursor()

cursor.execute('DELETE FROM site_scraper_sizing;')
cursor.execute('DELETE FROM site_scraper_imageurl;')
cursor.execute('DELETE FROM site_scraper_scrapedresult;')
cursor.execute('ALTER SEQUENCE site_scraper_sizing_id_seq RESTART 1;')
cursor.execute('ALTER SEQUENCE site_scraper_imageurl_id_seq RESTART 1;')

print('Database cleared successfully.')

connection.commit()