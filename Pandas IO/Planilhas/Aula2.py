import pandas as pd

#Retorna as páginas da planilha
print(pd.ExcelFile('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\emissoes_CO2.xlsx').sheet_names)

emissões = pd.read_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\emissoes_CO2.xlsx',sheet_name='emissoes_C02')
emissoes_percapita = pd.read_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\emissoes_CO2.xlsx',sheet_name='emissoes_percapita')
fontes = pd.read_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\emissoes_CO2.xlsx',sheet_name='fontes')
fontes_reduzidas = pd.read_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\emissoes_CO2.xlsx',sheet_name='fontes', usecols='A:C',nrows=1600)

print(fontes_reduzidas)
print(fontes.head(10))

# Salvando os arquivos

emissões.to_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\Planilhas/emissões.xlsx',index=False)
emissoes_percapita.to_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\Planilhas/Emissões_percapita.xlsx',index=False)
fontes.to_excel('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\Planilhas/fontes.xlsx',index=False)
