from urllib.request import urlopen
from xml.etree.ElementTree import parse #xml permite leer el rss como un diccionario
import pandas as pd
import json as js

company = 'gobierno'

newspapers = {
    'Expansion': 'https://e00-expansion.uecdn.es/rss/empresas.xml',
    'El economista': 'https://www.eleconomista.es/rss/rss-empresas.php',
    'Cinco dias': 'https://cincodias.elpais.com/seccion/rss/companias/',
    'El confidencial': 'https://rss.elconfidencial.com/empresas/'
}

tot_data = {
    'Periodico': [],
    'Empresa': [],
    'Noticia': [],
    'Fecha noticia': [],
    'Link Noticia': []
}

for i in newspapers:    # como newspapers es un diccionario, estoy recorriendo las claves
    url_str = newspapers[i]
    var_url = urlopen(url_str)
    xmldoc = parse(var_url)

    for item in xmldoc.iterfind('channel/item'):    #iteramos por el titulo dentro de cada noticia

        if company in item.findtext('title').lower(): # con and puedo añadir mas palabras para que cumplan la condición
            tot_data['Periodico'].append(i)
            tot_data['Empresa'].append(company)
            tot_data['Noticia'].append(item.findtext('title'))
            tot_data['Fecha noticia'].append(item.findtext('pubDate'))
            tot_data['Link Noticia'].append(item.findtext('link'))

company_df = pd.DataFrame(tot_data)
print("company_df.shape:", company_df.shape)
company_df.to_excel('./company_data.xlsx')
company_df.to_csv('./company_data.csv')
company_df.to_json("company_data.json")
print("\n FINISH \n")