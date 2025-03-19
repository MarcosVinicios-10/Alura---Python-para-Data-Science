#lendo e salvando uma tabela da wikipedia

import pandas as pd

dados = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')[0]
dados.drop('Unnamed: 0',axis=1,inplace=True)
print(dados)
dados.to_csv('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\HTML e XML\\tabela_paises.csv',index=False)
