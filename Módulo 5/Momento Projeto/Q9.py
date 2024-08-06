'''
9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar
se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
'''

gabarito = {1: 'A',
            2: 'B',
            3: 'C',
            4: 'B',
            5: 'A',
            6: 'D',
            7: 'C',
            8: 'C',
            9: 'A',
            10: 'B'}
nota = 0

for e in gabarito:
    resposta = input(f'Resposta da questão {e}:')
    if gabarito[e] == resposta:
        nota += 1
print(f'A nota do aluno é: {nota} pontos.')