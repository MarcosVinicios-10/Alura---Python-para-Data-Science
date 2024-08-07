'''
8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. 
Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
'''

doces = []
amargos = []

for e in range(1,11):
    id = int(input('Insira um ID, o ID precisa ser um número inteiro:'))
    if id%2 == 0:
        doces.append(id)
    else:
        amargos.append(amargos)
print(f'Temos {len(doces)} doces.\nTemos {len(amargos)} amargos.')
