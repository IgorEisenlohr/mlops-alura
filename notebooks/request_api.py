import requests

url = 'http://192.168.1.107:5000/preco/'

dados = {
    "tamanho":170,
    "ano":1999,
    "garagem":2
}
auth = requests.auth.HTTPBasicAuth('igor','3227Igor')
response = requests.post(url, json=dados, auth=auth)
if response.status_code == 200:
    print('Tudo certo com a API')
    print(response.json())
else:
    print('Erro na API')

