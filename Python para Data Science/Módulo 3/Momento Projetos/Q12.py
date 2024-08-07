'''
12 Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. 
Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

* do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
* valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
'''

combustivel = input('Hoje vai ser etanol ou disel(E/D)?')
litros = int(input('Quantos litros?'))

if combustivel == 'E':
    if litros <= 15:
        preço = litros * 1.70
        desconto = (preço * 2) / 100
        print(f'O preço é de {preço} e o desconto é de {desconto}, ficando no total: R${preço-desconto}')
    else:
        preço = litros * 1.70
        desconto = (preço* 4) / 100
        print(f'O preço é de {preço} e o desconto é de {desconto}, ficando no total: R${preço-desconto}')
elif combustivel == 'D':
    if litros <= 15:
        preço = litros * 2
        desconto = (preço * 3) / 100
        print(f'O preço é de {preço} e o desconto é de {desconto}, ficando no total: R${preço-desconto}')
    else:
        preço = litros * 2
        desconto = (preço * 5) / 100
        print(f'O preço é de {preço} e o desconto é de {desconto}, ficando no total: R${preço-desconto}')
else:
    print(f'Erro! "{combustivel}" não é válido.')
