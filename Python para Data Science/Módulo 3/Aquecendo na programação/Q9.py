# 9 Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = float(input('Digite um número: '))
A = int(numero)
if A == numero:
    print('É um número inteiro.')
else: 
    print('É um número decimal.')