"""
Web Scraper for https://beaugardsbbq.com/ 

Scrapes the Website --> Inputs Contents into a text file
"""

#virutalenv -> web_scrape

import requests
from bs4 import BeautifulSoup

menu_url = 'https://beaugardsbbq.com/menu'

menu_page = requests.get(menu_url)

soup = BeautifulSoup(menu_page.content, 'html.parser')

menu_title = soup.title.text


#Menu Section --> Appetizers, Sandwiches etc..
h3_tags = soup.find_all('h3', attrs={'data-ux': 'HeadingMiddle'})
menu_section = [h3.text for h3 in h3_tags]

#Menu_Items
h4_tags = soup.find_all('h4', attrs={'data-ux': 'HeadingMinor'})
menu_items = [h4.text for h4 in h4_tags]

#Prices
price_lst = soup.find_all(attrs={"data-ux": "PriceMajor"})
prices = [price.text for price in price_lst]

#Added Prices that were missing
prices[5] = '5 wings - 4.25, 10 wings - 8.25'
prices[8] = 'Pork - 5.25, Beef Brisket - 5.75'
prices[14] = 'Lunch Size - 8.25, Dinner Size 10.25'
prices[15] = 'Lunch Size - 8.95, Dinner Size 11.25'
prices[16] = 'Lunch Size - 10.45, Dinner Size 20.95'
prices[24] = '1/4 - 4.95, 1/2 - 9.75, 3/4 - 14.25, Full Slab - 18.95'
prices[27] = '1 Fillet - 6.75, 2 Fillets - 9.95'
prices[39] = 'Regular - 1.79, Large - 1.99'


#Grab Hour and Contact Information

main_url = 'https://beaugardsbbq.com/'

main_page = requests.get(main_url)

soup = BeautifulSoup(main_page.content, 'html.parser')


#Contact Section
find_p = soup.find_all('p')
address_info = [p.text for p in find_p]
address = address_info[1]
number = address_info[0]
open_hours = address_info[6]
closed_hours = address_info[7][:15]



# Write Contact information to a file
with open('contact.txt', 'w') as f:
    f.write('Beaugards Contact Information')
    f.write('\n')
    f.write('\n')
    f.write(f'Address\t{address}\n')
    f.write(f'Number\t{number}\n')
    f.write(f'Hours of Operation\n')
    f.write(f'Open\t{open_hours}\n')
    f.write(f'Closed\t{closed_hours}')
    f.close()



#Writes ALL Menu information to a file
with open('menu.txt', 'w') as f:
    f.write(menu_title[7:])
    f.write('\n')
    f.write('\n')
    for x in range(45):
        f.write(menu_items[x])
        f.write('\t')
        f.write(prices[x])
        f.write('\n')
    f.close()