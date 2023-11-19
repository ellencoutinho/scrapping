import requests
from bs4 import BeautifulSoup

url = 'https://franquias.portaldofranchising.com.br/franquias-de-alimentacao/?_gl=1*1dldi9q*_ga*NjI3MzYyODA4LjE2OTk5NTkzMTM.*_ga_TPGK1V9KED*MTcwMDM1MTM1Ni40LjEuMTcwMDM1MTM2Mi41NC4wLjA.'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
filtro1 = soup.find_all('a')
i = 0
for e in filtro1:
    if e.get('title'):
        if not ('#' in e.get('href')):
            i+=1
            print(e.get('title'))
            print(e.get('href'))

print(i)