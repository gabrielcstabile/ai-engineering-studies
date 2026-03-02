# Script para acessar a API do IBGE.

import requests
from pprint import pprint

nome = 'Ariel'

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

params = {
    'sexo':'M',
    'localidade': 33
}

resposta = requests.get(url, params=params)


try:
    resposta.raise_for_status()
    
except requests.HTTPError as e:
    pprint(f'Erro no request : {e}')
    resultado = None
    
else:
    resultado = resposta.json()

pprint(resultado)

