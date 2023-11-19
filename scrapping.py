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
            # [1]

print(i)

# Teste para a franquia hardcoded que seria pego em [1]
url_franquia = "https://franquias.portaldofranchising.com.br/franquia-kfc/"
page_franquia = requests.get(url_franquia)
soup = BeautifulSoup(page_franquia.text, 'html.parser')
n_unidades = soup.find_all('strong')[2].get_text()
contato = soup.find_all('strong')[3].get_text()

achou_investimento = False
achou_retorno = False
achou_contato = False
achou_faturamento = False
achou_unidades = False

faturamento = "Não informado"

for e in soup.find_all('strong'):
    conteudo = e.get_text()
    separacao_string = conteudo.split()
    if not achou_investimento and separacao_string[0] == 'a':
        investimento = conteudo
        achou_investimento = True
    elif not achou_retorno and separacao_string[0] == 'de':
        retorno = conteudo
        achou_retorno = True
    elif not achou_faturamento and separacao_string[0][0] == 'R':
        faturamento = conteudo
        achou_faturamento = True
    elif not achou_contato and len(separacao_string)==2:
        contato = conteudo
        achou_contato = True
    elif not achou_unidades:
        n_unidades = conteudo
        achou_unidades = True
print(f'investimento: {investimento}, retorno {retorno}, faturamento {faturamento}, n_unidades {n_unidades}, contato {contato}')