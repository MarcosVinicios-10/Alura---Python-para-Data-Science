'''
5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número
por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
'''
número = int(input('Digite um número inteiro:'))
fatorial = 0
x = número
for i in range(número -1, 0, -1):
    fatorial = (número * i)
    número = fatorial
print(f"O fatorial de {x} é {fatorial:,}.")
