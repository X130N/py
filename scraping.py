import requests #Modulo requests faz uma solicitação HTTP
from bs4 import BeautifulSoup as bs #Analisa o html retornado

github_user = input("Informe seu nome de usuario do github: ")
url = 'https://github.com/' + github_user

#envia uma requisição GET para a URL do perfil de um usuário e armazena na variavel 'r'
r = requests.get(url)

#utiliza a biblioteca BeautifulSoup para analisar e interpretar o conteúdo HTML que foi obtido e armazenado na variável r através da requisição HTTP GET, agora a 'soup' contém o HTML da página web interpretado e estruturado
soup = bs(r.content, 'html.parser')


profile_image = soup.find('img', {'class' : 'avatar'})['src']
#soup: É a variável que contém o HTML analisado da página web
#.find(): É um método da BeautifulSoup que é usado para buscar a primeira ocorrência de um elemento no HTML que corresponde aos critérios especificados.
#'img': Este é o primeiro argumento do método find e indica que estamos procurando por um elemento de imagem (tag <img> em HTML).
#{'class' : 'avatar'}: Este é o segundo argumento, que é um dicionário especificando atributos adicionais que o elemento <img> deve ter. Neste caso, estamos procurando por uma imagem (<img>) que tenha uma classe (class) chamada 'avatar'.
#['src']: Após localizar o elemento <img> com a classe 'avatar', o código acessa o valor do atributo 'src' desse elemento. O atributo src em uma tag <img> normalmente contém o URL da imagem.
#O resultado, que é o URL da imagem de perfil do usuário, é  armazenado na variável profile_image.

print(profile_image)