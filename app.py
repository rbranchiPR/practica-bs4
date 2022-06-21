from unittest import result
import requests
from bs4 import BeautifulSoup

peticion = requests.get("https://www.neogol.com/maximos-goleadores-historicos-de-la-champions-league/")
soap = BeautifulSoup(peticion.content, 'html.parser')

ol_object = soap.find('ol')

for object in ol_object.findChildren('h3'):
    print(object.strong.contents[0])

# EJEMPLO POO

class Results:
    def __init__(self, url:str):
        self.url = url
        self.page = requests.get(url)
    
    def get_results(self):
        home_results = BeautifulSoup(self.page.text, 'html.parser')
        results = home_results.find('ol')

        for result in results.findChildren("li"):
            print(result.strong.contents[0])

champions_league = Results('https://www.neogol.com/maximos-goleadores-historicos-de-la-champions-league/')
champions_league.get_results()

# HACER WEBSCRAPING A: https://es-la.facebook.com/ & OBTENER LOS IDIOMAS DISPONIBLES DE FACEBOOK