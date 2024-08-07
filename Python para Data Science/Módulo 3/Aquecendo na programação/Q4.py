# 4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

ano1 = float(input('Qual a média do primeiro ano?'))
ano2 = float(input('Qual a média do segundo ano?'))
ano3 = float(input('Qual a média do terceiro ano?'))

if ano1 >= ano2 and ano1 >= ano3:
    print(f'O maior valor é: {ano1}')
elif ano2 >= ano3 and ano2>ano1:
    print(f'O maior  valor é: {ano2}')
else:
    print(f'O maior valor é {ano3}!')

