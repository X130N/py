import requests
from bs4 import BeautifulSoup as bs

github_user = input("Informe seu nome de usuario do github: ")
url = 'https://github.com/' + github_user

r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'class' : 'avatar'})['src']
print(profile_image)