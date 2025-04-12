#!/usr/bin/python3

import sys
import argparse

import pagegetter
import parser



ap = argparse.ArgumentParser()
ap.add_argument('pokemon', help='Pokemon to lookup. Takes either name or Nat. Dex number')
ap.add_argument('generation', help='Generation to check against. (1~9)')
ap.add_argument('-c', '--clean', help='clean the cache', action='store_true')



args = ap.parse_args()

args.generation = int(args.generation)

if args.generation not in range(5):
    print("Wrong value for generation!")
    sys.exit()


if args.clean:
    print("Cleaning cache")
    pagegetter.clean_cache()
    sys.exit()


check_val = 25
if args.pokemon:
    try:
        check_val = int(args.pokemon)
    except ValueError:
        check_val = args.pokemon


data = pagegetter.get_page(pagegetter.URL_NATIONAL_DEX)
nat_parser = parser.NationalDexListParser(data, args.generation)
pokemon_list = nat_parser.make_pokemon_list()

did_process = False
for pokemon in pokemon_list:
    if pokemon.num == check_val or pokemon.name == check_val:
        did_process = True
        print(pokemon)
        print(pokemon.page_link)
        print(pokemon.learnset_link)

        learnset_page_data = pagegetter.get_page(pokemon.learnset_link)
        learnset = parser.LearnsetParser(learnset_page_data).make_learnset()
        print("Level Up")
        for entry in learnset.level_up:
            print(entry)

if not did_process:
    raise Exception("Pokemon does not exist!")