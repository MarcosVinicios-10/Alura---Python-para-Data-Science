# 1. Escreva um programa que peça à pessoa usuária para fornecer dois números e exiba o número maior.

n1 = int(input('Digite um número: '))
n2 = int(input('Outro: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}.')
else:
    print(f'{n2} é maior que {n1}.')