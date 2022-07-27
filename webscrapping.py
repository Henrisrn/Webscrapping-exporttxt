# On importe la fonction 'get' (téléchargement) de 'requests' 
# Et la classe 'Selector' (Parsing) de 'scrapy'
from requests import get
from scrapy import Selector
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request
import csv
import requests
# Lien de la page à scraper
features="lxml"
url = "https://www.worldometers.info/world-population/population-by-country/"
#url = "https://www.frankfurt-airport.com/wartezeiten/public?lang=en"
req = requests.get(url)
soup = bs(req.text, 'html.parser')

#To get the element by ID
print(soup.find(id="wartezeiten"))

#To get all the element of a type
print(soup.find_all('a'))

b = open('TestSortie.txt', 'w')
b.write(str(soup))

data = soup.find_all("table")[0]
print(data)
df_population = pd.read_html(str(req.text))[0]
print(df_population.head())
