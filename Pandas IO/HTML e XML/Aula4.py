import pandas as pd

# Lendo e salvando html

url = 'https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies'
dados_html = pd.read_html(url)[1]
print(dados_html)
dados_html.to_html('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\HTML e XML\melhores_filmes.html',index=False)

#Lendo e salvando XML

dados_xml = pd.read_xml('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\imdb_top_1000.xml')
dados_xml.to_xml('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\HTML e XML\melhores_1000_filmes.xml',index=False)
print(dados_xml)
