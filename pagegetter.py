import os
import shutil
import requests

PAGE_CACHE_PATH = os.path.expanduser("~/.poke-scrape/cache/")
URL_BASE = "https://bulbapedia.bulbagarden.net/wiki/"
URL_NATIONAL_DEX = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

def clean_cache():
    shutil.rmtree(PAGE_CACHE_PATH)

def _url_to_cache_page_name(url):
    file_name = "page_" + url.replace(URL_BASE, "")
    file_name = file_name.replace("/", "_")
    return file_name


def get_page(url):
    os.makedirs(PAGE_CACHE_PATH, exist_ok=True)

    file_name = _url_to_cache_page_name(url)
    file_path = PAGE_CACHE_PATH + file_name

    if os.path.exists(file_path):
        print("File exists! Returning cached page.")

        with open(file_path, 'r') as file:
            data = file.read()
        return data
    
    else:
        print("File does not exists. Fetching from url.")

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'x') as file:
                file.write(response.text)
            return response.text
        
    return ""

ROMAN_NUMERAL_LOOKUP = ['N/A', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
def construct_learnset_page_url_for_pokemon(pokemon_page, gen_number):
    roman_numeral_string = ROMAN_NUMERAL_LOOKUP[gen_number]
    return f"{pokemon_page}/Generation_{roman_numeral_string}_learnset"