import pandas as pd
import requests
from bs4 import BeautifulSoup

colunas = ['Nome', 'Unidades', 'Investimento', 'Retorno', 'Faturamento', 'Contato']
df = pd.DataFrame(columns=colunas)

url = 'https://franquias.portaldofranchising.com.br/franquias-de-alimentacao/?_gl=1*1dldi9q*_ga*NjI3MzYyODA4LjE2OTk5NTkzMTM.*_ga_TPGK1V9KED*MTcwMDM1MTM1Ni40LjEuMTcwMDM1MTM2Mi41NC4wLjA.'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
filtro1 = soup.find_all('a')
i = 0
for e in filtro1:
    if e.get('title'):
        if not ('#' in e.get('href')):
            i+=1
            nome = e.get('title')
            url_franquia = e.get('href')
            page_franquia = requests.get(url_franquia)
            soup = BeautifulSoup(page_franquia.text, 'html.parser')

            achou_unidades = False
            achou_investimento = False
            achou_retorno = False
            achou_contato = False
            achou_faturamento = False

            faturamento = "Não informado"

            for e in soup.find_all('strong'):
                conteudo = e.get_text()
                separacao_string = conteudo.split()
                if not achou_investimento and separacao_string[0] == 'a':
                    investimento = ' '.join(separacao_string)
                    achou_investimento = True
                elif not achou_retorno and separacao_string[0] == 'de':
                    retorno = ' '.join(separacao_string)
                    achou_retorno = True
                elif not achou_faturamento and separacao_string[0][0] == 'R':
                    faturamento = ' '.join(separacao_string)
                    achou_faturamento = True
                elif not achou_contato and len(separacao_string)==2:
                    contato = ' '.join(separacao_string)
                    achou_contato = True
                elif not achou_unidades:
                    n_unidades = ' '.join(separacao_string)
                    achou_unidades = True
            print(f'investimento: {investimento}, retorno {retorno}, faturamento {faturamento}, n_unidades {n_unidades}, contato {contato}')
            
            dados = {
                'Nome':nome,
                'Unidades':n_unidades,
                'Investimento':investimento,
                'Retorno':retorno,
                'Faturamento':faturamento,
                'Contato':contato

            }
            df = df._append(dados, ignore_index=True)

            # [1]

print(i)
print(df)

# Teste para a franquia hardcoded que seria pego em [1]


