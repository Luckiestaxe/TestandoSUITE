from requisicoes import *
import re

# RECUPERA INFORMAÇÕES DO JSON (CREDENCIAIS)

json_path = 'credenciais-prd.json'
data = get_json_data(json_path)
url_base = data.get('url_base')
client_id = data.get('client_id')
client_secret = data.get('client_secret')

# RECUPERA O TOKEN PARA SER USADO NAS CHAMADAS DA API
token_data = get_token_data(url_base, client_id, client_secret)
access_token = token_data['access_token']

# Passa o NUP
#24001.003813/2025-76
#13001.031273/2024-13
valor = re.sub(r'\D', '', '13001.031273/2024-13')

resultado = get_processo_por_nup(access_token, url_base, nup=valor)
#print(resultado)


tipodocs = get_tipodocs(access_token,url_base)
for i in range(0,len(tipodocs)):
    print(tipodocs[i])

#lotacoes = get_lotacoes(access_token, url_base)
#for i in range(0,len(lotacoes)):
# print(lotacoes[i]['id'],lotacoes[i]['entity']['name'],lotacoes[i]['description'])

#assuntos = get_assuntos(access_token,url_base)
#for i in range(0,len(assuntos)):
#    print(assuntos[i])

