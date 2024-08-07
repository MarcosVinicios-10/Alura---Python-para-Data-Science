# 6 Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

dia = int(input('Digite o dia: '))
mês = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if 31 >= dia >= 1:
    if 12 >= mês >= 1:
        if ano >= 2000:
            print(f'Tudo certo! {dia:02d}/{mês:02d}/{ano}')
        else:
            print(f'Ano inválido!')
    else:
        print('Mês inválido!')
else:
    print('Dia inválido!')