'''
7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas
por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''
while True:
    número = int(input('Insira um número inteiro ou 0 para sair:'))
    if número == 0:
        break
    elif número == 2:
        print(f'{número} é primo.')
    elif número <= 1:
        print(f'{número} não é primo')
    for e in range(2, número):
        resto = número%e
        if resto == 0:
            print(f'{número} não é primo.')
            break
        elif e == número - 1:
            print(f'{número} é primo.')
            break
