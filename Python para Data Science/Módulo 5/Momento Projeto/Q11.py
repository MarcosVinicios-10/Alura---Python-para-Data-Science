'''
11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Escreva um código que calcule o total de vendas e o produto mais vendido.
'''

vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
          'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total = sum(vendas.values())
maior = max(vendas.values())
print(f'Total de vendas: {total}')
for e in vendas:
    if vendas[e] == maior:
        print(f'O produto mais vendido foi o "{e}".')
        break