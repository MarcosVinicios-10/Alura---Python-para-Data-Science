'''
1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

3) Confira a quantidade de linhas e colunas desse DataFrame.

4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.
'''
import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url,sep=',')
print(dados.head(7))
print(dados.tail(5))
print(dados.info())
print(dados.describe())

'''
1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.

2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.

3) Aplique um filtro que selecione apenas os alunos que foram aprovados.

4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".

Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. 
Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.
'''
# Tratando os nulos.
dados.fillna(0,inplace=True)

# Removendo Alice e Carlos.
dados.query('not(Nome == "Carlos" | Nome == "Alice")',inplace=True)

# Apenas aprovados
aprovados = dados.query('Aprovado == True')

# Extra
aprovados = aprovados.replace(7,8)
print(aprovados)

# Salvando
aprovados.to_csv('Aprovados.csv',index=False,sep=',')

