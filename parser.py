from bs4 import BeautifulSoup

URL_BASE_LINK_ADDER = "https://bulbapedia.bulbagarden.net"

def parse_national_dex_page_into_regional_lists(webpage_data):
    soup = BeautifulSoup(webpage_data, 'html.parser')

    regional_lists = list()

    tables = soup.find_all('table')
    for table in tables:
        if table.has_attr('class') and table['class'][0] == 'roundy':
            regional_lists.append(table)

    return regional_lists


def _tr_is_pokemon(tr_soup):
    return tr_soup.has_attr('style')

def _tr_is_alt_form(tr_soup):
    td = tr_soup.find_all('td')
    return (not td[0].has_attr('rowspan'))

def _make_entry_from_tr(tr_soup):
    td2 = tr_soup.find_all('td')[2]
    a = td2.a
    return {
        'name': a.text,
        'link': URL_BASE_LINK_ADDER + a.get('href'),
    }

def parse_regional_dex_list_into_entries(regional_dex_soup):
    entry_list = list()

    trs = regional_dex_soup.find_all('tr')
    for tr in trs:
        if _tr_is_pokemon(tr) and not _tr_is_alt_form(tr):
            entry_list.append(_make_entry_from_tr(tr))

    return entry_list
