'''
3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5
de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
'''

notas = []
x = 0

while x < 15:
    nota = float(input('Insira uma nota de 0 a 5: '))
    if nota >= 0 and nota <= 5:
        notas.append(nota)
        x += 1
    else:
        print('Erro! insira uma nota válida!')
print(notas)
