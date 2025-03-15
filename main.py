#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')
    for table in tables:
        if table.has_attr('class') and table['class'][0] == 'roundy':
            print("============================================")
            print("Entry:", table)
            print("")
            print("")

else:
    print("Get failed with status code: ", response.status_code)

