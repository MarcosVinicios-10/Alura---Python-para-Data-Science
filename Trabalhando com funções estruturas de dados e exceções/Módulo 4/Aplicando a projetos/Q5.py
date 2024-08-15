'''
5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado 
para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". 
O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:
gabarito = ['D', 'A', 'B', 'C', 'A']

Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. 
Por exemplo, 1 not in [2,3,4]... Saída: True.
Notas sem exceção:

'''

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calculaNota(respostas):
    try:
        gabarito = ['D', 'A', 'B', 'C', 'A']
        for i in range(len(respostas)):
            for c in range(len(respostas[i])):
              if respostas[i][c] not in gabarito:
                raise ValueError
    except ValueError:
        print(f'{ValueError}, A alternativa {respostas[i][c]} não é uma opção de alternativa válida.')
    else:
       notas = [[0],[0],[0]]
       for x in range(len(respostas)):
          for y in range(len(gabarito)):
             if respostas[x][y] == gabarito[y]:
                notas[x][0] = (notas[x][0] + 1)
       return notas
        
             
print(calculaNota(testes_com_ex))
