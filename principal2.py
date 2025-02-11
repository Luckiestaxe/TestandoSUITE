from requisicoes import *
import re
import base64

# RECUPERA INFORMAÇÕES DO JSON (CREDENCIAIS)

json_path = 'credenciais-hml.json'
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
#31032.005819/2024-03 
#31032.011272/2024-77
#31032.007234/2024-10

#valor = re.sub(r'\D', '', '31032.007234/2024-10')

#resultado = get_processo_por_nup(access_token, url_base, nup=valor)
#print(resultado)

arquivo = open('teste.txt',"rb")
dados = arquivo.read()

dadosbase64 = base64.urlsafe_b64encode(dados).decode("utf-8")

#print((dadosbase64))

arquivo = {
    'file': dadosbase64,
    'document_type_id': 77,
    'file_name': 'teste',
    'file_type': 'base64'
}

dados = {
    'subject_id': 965,
    'origin_id': 10292,
    'capacity_id': 10219,
    'files': [  
        {
        'file': dadosbase64,
        'document_type_id': 77,
        'file_name': 'teste',
        'file_type': 'base64'
        }   
    ],
    'system_name': 'laboratório de grafos e inteligência computacional'
}

post_processo(access_token, url_base, dados)


#tipodocs = get_tipodocs(access_token,url_base)
#for i in range(0,len(tipodocs)):
#    print(tipodocs[i])




#lotacoes = get_lotacoes(access_token, url_base)
#print(lotacoes[1].items())
#print(type(lotacoes[1]),len(lotacoes[1]),lotacoes[1].keys(),type(lotacoes[1].keys()))
#for i in range(0,len(lotacoes)):
# print(str(lotacoes[i]['id'])+' | '+lotacoes[i]['description']+' | '+lotacoes[i]['abbreviation']+' | '+lotacoes[i]['entity']['name']+' | '+lotacoes[i]['entity']['abbreviation'])
# print(lotacoes[i]['id'],lotacoes[i]['entity']['name'],lotacoes[i]['description'])




#assuntos = get_assuntos(access_token,url_base)
#for i in range(0,len(assuntos)):
#    print(assuntos[i])

