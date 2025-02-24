import pandas as pd
import chardet

url = 'https://raw.githubusercontent.com/alura-cursos/pandas/refs/heads/main/superstore_data.csv'

dados = pd.read_csv(url) 
# Selecionando apenas as 1200 primeira linha e 3 colunas(posso usar índices)
dados_reduzido = pd.read_csv(url,nrows=1200,usecols=['Year_Birth','Education','Income']) 

#salvando

dados_reduzido.to_csv('dados_reduzido.csv',index=False)

# Desafio Fazer a leitura correta

#Verificando encoding do arquivo
with open('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\dados_sus.csv', 'rb') as file:
    print(chardet.detect(file.read()))

sus = pd.read_csv('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\dados_sus.csv',skiprows=3,skipfooter=9,sep=';',encoding='ISO-8859-1',engine='python')
print(sus)