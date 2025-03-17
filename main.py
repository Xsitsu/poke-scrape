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



check_num = 176

data = pagegetter.get_page(pagegetter.URL_NATIONAL_DEX)
nat_parser = parser.NationalDexListParser(data)
pokemon_list = nat_parser.make_pokemon_list()

for pokemon in pokemon_list:
    if pokemon.num == check_num:
        print(pokemon)
