'''
8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de 
clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
'''

até_25 = 0
até_50 = 0
até_75 = 0
até_100 = 0

while True:
    idade = int(input('Insira uma idade:'))
    
    if idade < 0:
        break
    elif 0 <= idade <= 25:
        até_25 += 1
    elif 26 <= idade <= 50:
        até_50 += 1
    elif 51 <= idade <= 75:
        até_75 += 1
    elif 76 <= idade <= 100:
        até_100 += 1
    else:
        print('Insira uma idade menor que 100.')
print(f'A distribuição de idade ficou da seguinte maneira:\nEntre 0-25:\t {até_25}.\nEntre 26-50:\t {até_50}.\nEntre 51-75:\t {até_75}.\nEntre 76-100:\t {até_100}.')
 