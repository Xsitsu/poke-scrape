from bs4 import BeautifulSoup

from pokemon import Pokemon
import learnset
import move
import pagegetter

URL_BASE_LINK_ADDER = "https://bulbapedia.bulbagarden.net"



class NationalDexListParser:
    def __init__(self, page_data, generation_num):
        self.page_data = page_data
        self.generation_num = generation_num
    
    def make_pokemon_list(self):
        pokemon_list = list()

        regional_lists = self._parse_national_dex_page_into_regional_lists()
        for i in range(4):
            pokemon_list.extend(self._parse_regional_dex_list_into_entries(regional_lists[i]))
        
        return pokemon_list

    def _parse_national_dex_page_into_regional_lists(self):
        soup = BeautifulSoup(self.page_data, 'html.parser')

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
        learnset_link = pagegetter.construct_learnset_page_url_for_pokemon(link, self.generation_num)
        return Pokemon(num, name, link, learnset_link)

    def _parse_regional_dex_list_into_entries(self, regional_dex_soup):
        entry_list = list()

        trs = regional_dex_soup.find_all('tr')
        for tr in trs:
            if self._tr_is_pokemon(tr) and not self._tr_is_alt_form(tr):
                entry_list.append(self._make_pokemon_from_tr(tr))

        return entry_list


class LearnsetParser:
    def __init__(self, page_data):
        self.page_data = page_data
    
    def make_learnset(self):
        soup = BeautifulSoup(self.page_data, 'html.parser')

        sortable_tables = list()

        tables = soup.find_all('table')
        for table in tables:
            if table.has_attr('class'):
                print(f"table with class: '{table['class']}'")
                if table['class'][0] == 'sortable':
                    sortable_tables.append(table)
                    print("adding sortable table~!")
        
        table_rows = sortable_tables[0].tbody.find_all('tr')[1:]

        learn_set = learnset.Learnset()
        for tr in table_rows:
            learn_set.level_up.append(self._make_level_up_entry(tr))
        
        return learn_set


    def _get_move_start_index(self, tds):
        index = 0
        for td_soup in tds:
            if len(td_soup.find_all('a')) > 0:
                return index
            index += 1
        raise Exception('Could not find start of move in entry!')


    def _extract_level_from_td(self, td):
        return td.span.text

    def _make_move_from_td_list(self, tds):
        move_name = tds[0].find_all('span')[0].text
        move_type = tds[1].find_all('span')[0].text
        power = tds[2].find_all('span')[0].text
        accuracy = tds[3].find_all('span')[0].text
        pp = tds[4].text

        return move.Move(move_name, move_type, power, accuracy, pp)


    def _make_level_up_entry(self, tr_soup):
        tds = tr_soup.find_all('td')
        move_start_index = self._get_move_start_index(tds)
        if move_start_index == None:
            return
        
        level_list = list()
        for i in range(move_start_index):
            level_list.append(self._extract_level_from_td(tds[i]))
        
        move = self._make_move_from_td_list(tds[move_start_index:])
        return learnset.LevelUpEntry(level_list, move)