import requests
import json

def get_json_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def get_token_data(url_base, client_id, client_secret):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    url = f'{url_base}/customer/get-token/'
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        return token_data
    else:
        print(f"Erro: {response.status_code}")
        print(response.text)
        return None

def get_tipodocs(access_token, url_base):
    url = f'{url_base}/process/file/type/list/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None



def get_lotacoes(access_token, url_base):
    url = f'{url_base}/control/capacity/public/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_assuntos(access_token, url_base):
    url = f'{url_base}/control/subject/all/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_processos_arquivados_por_cpf(access_token, url_base, cpf):
    url = f'{url_base}/process/cc/archived/{cpf}/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_processos_nao_arquivados_por_cpf(access_token, url_base, cpf):
    url = f'{url_base}/process/cc/{cpf}/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_andamentos(access_token, url_base):
    url = f'{url_base}/process/file/type/list/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_processo_por_nome(access_token, url_base):
    url = f'{url_base}/process/cc/name/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        print(response.text)
        return None


def get_processo_por_nup(access_token, url_base, nup):
    url = f'{url_base}/process/nup/{nup}/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        print(response.text)
        return None

#sem funcionar
def get_historia_processo_por_nup(access_token, url_base, nup):
    url = f'{url_base}/process/public-history/{nup}/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

#sem funcionar
def get_processos_filtrados(access_token, url_base):
    url = f'{url_base}/process/list-by-filters/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json; version=1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
