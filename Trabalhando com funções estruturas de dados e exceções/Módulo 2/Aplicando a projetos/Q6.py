'''
6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
'''

def desempenho(x):
    maior = max(x)
    menor = min(x)
    média = sum(x)/len(x)
    if média >= 6:
        situação = 'aprovado'
    else:
        situação = 'reprovado'
    
    return média, maior, menor, situação # Não retorna uma lista

nota = []
for i in range(1,5):
    nota.append(float(input('Digite uma nota: ')))

estatisticas = list(desempenho(nota))

print(f'O(a) estudante obteve uma média de {estatisticas[0]}, com a sua maior nota de {estatisticas[1]} pontos e a menor nota de {estatisticas[2]} pontos e foi {estatisticas[3]}')
