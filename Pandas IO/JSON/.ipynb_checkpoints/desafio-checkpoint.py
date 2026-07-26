import pandas as pd
import requests

dados = (requests.get('https://jsonplaceholder.typicode.com/users')).json()
dados = pd.json_normalize(dados)
print(dados)
dados.to_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\JSON\dados_api.xlsx',index=False)