import pandas as pd

'''
Para ler uma planilha do google é necessário apagar tudo após o id e colocar os parâmetros /gviz/tq?tqx=out:csv se quisermos páginas especificas bastas adicionar
&sheet=nome
'''

url = 'https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/gviz/tq?tqx=out:csv'
url2 = 'https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/gviz/tq?tqx=out:csv&sheet=fontes'


dados = pd.read_csv(url)
fontes = pd.read_csv(url2)
print(dados)
print(fontes)


# Desafio ler e salvar

url_dados = 'https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/gviz/tq?tqx=out:csv'

emissões_mundo = pd.read_csv(url_dados)
emissões_mundo.to_csv('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\Planilhas\emissões_mundo.csv',index=False)
