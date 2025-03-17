from bs4 import BeautifulSoup

from pokemon import Pokemon

URL_BASE_LINK_ADDER = "https://bulbapedia.bulbagarden.net"



class NationalDexListParser:
    def __init__(self, page_data):
        self.page_data = page_data
    
    def make_pokemon_list(self):
        pokemon_list = list()

        regional_lists = self._parse_national_dex_page_into_regional_lists()
        for i in range(4):
            pokemon_list.extend(self._parse_regional_dex_list_into_entries(regional_lists[i]))
        
        return pokemon_list

    def _parse_national_dex_page_into_regional_lists(self):
        soup = BeautifulSoup(self.page, 'html.parser')

        regional_lists = list()

        tables = soup.find_all('table')
        for table in tables:
            if table.has_attr('class') and table['class'][0] == 'roundy':
                regional_lists.append(table)

        return regional_lists

    def _tr_is_pokemon(self, tr_soup):
        return tr_soup.has_attr('style')

    def _tr_is_alt_form(self, tr_soup):
        td = tr_soup.find_all('td')
        return (not td[0].has_attr('rowspan'))

    def _make_pokemon_from_tr(self, tr_soup):
        tds = tr_soup.find_all('td')

        num_text = tds[0].text

        a = tds[2].a

        num = int(num_text[1:])
        name = a.text
        link = URL_BASE_LINK_ADDER + a.get('href')
        return Pokemon(num, name, link)

    def _parse_regional_dex_list_into_entries(self, regional_dex_soup):
        entry_list = list()

        trs = regional_dex_soup.find_all('tr')
        for tr in trs:
            if self._tr_is_pokemon(tr) and not self._tr_is_alt_form(tr):
                entry_list.append(self._make_pokemon_from_tr(tr))

        return entry_list
