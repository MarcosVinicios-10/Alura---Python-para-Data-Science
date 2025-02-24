'''
1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.

2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras.

3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.
'''
import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url,sep=',')
dados.fillna(0,inplace=True)
dados['Pontos_extras'] = dados['Notas'].apply(lambda x: (x*40)/100)
dados['Notas_finais'] = dados['Notas'] + dados['Pontos_extras']
dados['Aprovado_final'] = dados['Notas_finais'].apply(lambda x: True if x>=6 else False)
Aporvados_pontosEx = dados.query("Aprovado == False & Aprovado_final == True")
print(Aporvados_pontosEx)
print(dados)