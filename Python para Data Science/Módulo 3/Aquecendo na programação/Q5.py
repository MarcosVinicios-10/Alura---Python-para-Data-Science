# 5 Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

produto1 = float(input('Qual o preço  do primeiro produto?'))
produto2 = float(input('Qual o preço do segundo produto?'))
produto3 = float(input('Qual o preço do terceiro produto?'))

if produto1 <= produto2 and produto1 <= produto3:
    print(f'O menor valor é: R${produto1}')
elif produto2 <= produto3 and produto2<produto1:
    print(f'O menor valor é: R${produto2}')
else:
    print(f'O menor valor é R${produto3}!')
