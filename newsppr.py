import requests
from bs4 import BeautifulSoup as bs

def news():
    i = 0
    result = []
    url = 'https://ria.ru/lenta/'

    source_code = requests.get(url)
    html = bs(source_code.text, 'html.parser')
    countdown = html.find_all('meta', {"itemprop": "name"})
    
    for new in countdown:
        i = i + 1
        if i != 2 and i != 3 and i != 4 and i < 10:
            result.append(((str(new)[15:-19])))
            result.append('')
    return (str(result)[2:-2]).replace("\', \'", '\n')
print(news())
