#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser



ap = argparse.ArgumentParser()
ap.add_argument('-c', '--clean', help='clean the cache', action='store_true')
args = ap.parse_args()



if args.clean:
    print("Cleaning cache")
    pagegetter.clean_cache()
    sys.exit()




data = pagegetter.get_page(pagegetter.URL_NATIONAL_DEX)

regional_lists = parser.parse_national_dex_page_into_regional_lists(data)

for i in range(4):
    entries = parser.parse_regional_dex_list_into_entries(regional_lists[i])
    print("Region:", i)
    for entry in entries:
        print("Pokemon:", entry)