import requests

#Captura de cabeçalho http


captura_url = input('Informe aqui a url: ')

response = requests.get(captura_url)

if response.status_code == 200: #Verifica se o codigo de status é igual a 200, "Status_code: 200" é igual a "OK"
    headers = response.headers
    
    for chave, valor in headers.items():#Usado laço for, para imprimir cada chave e valor dos cabeçalhos.
        print(f'{chave} - {valor}')
else: #Caso o status_code não for um "OK", retorna uma mensagem informando que não foi possivel estabelecer uma conexão
    print(f'O código de status é -{response.status_code}, portanto, não foi possivel estabelecer uma conexão!')