# 8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

n1 = int(input('Vamos calcular o resto da divisão, digite o numerador:'))
n2 = int(input('Agora o denominador, mas atenção! ele não pode ser 0:'))
print(f'O resto divisão é: {n1%n2}')
