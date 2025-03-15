#!/usr/bin/python3

from bs4 import BeautifulSoup

import pagegetter


data = pagegetter.get_page(pagegetter.URL_NATIONAL_DEX)

soup = BeautifulSoup(data, 'html.parser')


tables = soup.find_all('table')
for table in tables:
    if table.has_attr('class') and table['class'][0] == 'roundy':
        print("============================================")
        print("Entry:", table)
        print("")
        print("")
