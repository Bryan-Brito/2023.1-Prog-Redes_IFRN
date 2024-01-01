import requests

#url a para solicitacao
url = 'http://www.ifrn.edu.br'

#requisição HTTP GET
response = requests.get(url)

#imprimir o codigo de 
print('Status code:', response.status_code)
print('Response:')
print(response.text)