'''
1) Calcular a média de quartos por apartamento;

2) Conferir quantos bairros únicos existem na nossa base de dados;

3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;

4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
'''

import pandas as pd
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url,sep=';')

# média
média_apartamentos = (dados.query("Tipo == 'Apartamento'")).groupby('Tipo')[['Quartos']].mean()
print(média_apartamentos)

#Bairros únicos
bairros_unicos = dados.Bairro.unique()
print(bairros_unicos)

# Média de aluguel mais alta por bairro

média_aluguel_bairro = dados.groupby('Bairro')[['Valor']].mean().sort_values('Valor')
print(média_aluguel_bairro)

# Gráfico das 5 maiores médias

média_aluguel_bairro.tail(5).plot(kind='barh', color='turquoise', xlabel='Média de Aluguel',ylabel='Bairro')
plt.show()