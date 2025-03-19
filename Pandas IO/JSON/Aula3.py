import pandas as pd
import json

pacientes = pd.read_json('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\pacientes.json')
pacientes2 = pd.read_json('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\pacientes_2.json')

# trazendo os dados aniados os dados para um data frame

pacientes2 = pd.json_normalize(pacientes2['Pacientes'])
print(pacientes2.columns)

# trazendo as colunas pesquisa e ano

with open('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\pacientes_2.json','r',encoding='utf-8') as file:
    pacientes2 = json.loads(file.read())

pacientes2 = pd.json_normalize(pacientes2,record_path=['Pacientes'],meta=['Pesquisa','Ano'])
print(pacientes2.columns)

# salvando

pacientes2.to_json('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\JSON\pacientes_normalizado.json',orient='records')

