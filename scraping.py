import pandas as pd
import regex as re
from bs4 import BeautifulSoup
import requests

# Codigo por @simonamador

# El siguiente codigo extrae las descripciones de las primeros primeros 
# productos mas populares en la categoria 'laptops' de Mercado Libre.
# Se trabaja con BeautifulSoup para web scraping

# Se obtienen los urls de los productos desde la pagina de categoria de
# 'laptops'.
url = 'https://listado.mercadolibre.com.pe/laptops#menu=categories'
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# Nota. Se guardan los primeros 15 caracteres del nombre del producto, 
# ya que contienen la marca del producto
laptops = [(a['href'], a.get_text()[:15]) for a in soup.find_all('a',class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')]

# Se inicializa la lista de las descripciones
desc= []

# Por cada link de un producto, se extrae la descripcion y se guarda en la lista.
for uniqlink in laptops:
    response = requests.get(uniqlink[0])
    web_page = response.text
    uniq_soup = BeautifulSoup(web_page, "html.parser")
    desc.append(([a.get_text() for a in uniq_soup.find_all('p',class_="ui-pdp-description__content")], uniqlink[1]))

# Se genera un dataframe con los datos
df = pd.DataFrame(desc, columns=['Desc','Laptop'])

# Regex con la extraccion de marcas reconocidas
brands = '[Hh][Pp]|[Ll]enovo|LENOVO|[Aa]sus|[Mm]acbook|[Tt]hinkpad|[Dd][Ee][Ll][Ll]|[Hh]uawei'

# Se extrae el texto de descripciones y los nombres de las marcas reconocidas
df['Desc'] = df['Desc'].map(lambda x: x[0] if len(x)>0 else 0)
df['Laptop'] = df['Laptop'].map(lambda x: re.findall(brands,x)[0] if len(re.findall(brands,x))>0 else 'Otro')
df['Laptop'] = df['Laptop'].map(lambda x: 'Hp' if x == 'HP' else x)
# Se guardan los resultados
df.to_csv('desc_data.csv')