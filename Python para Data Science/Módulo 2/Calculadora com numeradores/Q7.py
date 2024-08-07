# 7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

n1 = int(input('Vamos fazer uma divisão inteira, digite o numerador:'))
n2 = int(input('Agora o denominador, mas atenção! ele não pode ser 0:'))
print(f'A divisão é: {n1//n2}')
