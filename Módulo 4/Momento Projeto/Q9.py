'''
9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. 
A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
'''
candidato1 = 0
candidato2 = 0 
candidato3 = 0
candidato4 = 0
branco = 0
nulo = 0

for e in range(1,21):
    voto = int(input(f'Digite o voto de número {e}: '))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
print(f'Resultado da elição:\nCandidato 1:\t{candidato1}.\nCandidato 2:\t{candidato2}.\nCandidato 3:\t{candidato3}.\nCandidato 4:\t{candidato4}.')
votos = [candidato1, candidato2, candidato3, candidato4]
maior = max(votos)
posição = votos.index(maior)
x = posição + 1
print(f'O vencedor foi o candidato {x}.')
