'''
10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar.
O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
'''
operação = input('Escolha uma operação: Soma, Subtração, Divisão ou Multiplicação: ')
numero1 = float(input("Qual o primeiro número? "))
numero2 = float(input("Qual o segundo número? "))
Certo = False

if operação == 'Soma':
    operação = numero1 + numero2
    inteiro = int(operação)
    if inteiro == operação:
        inteiro_ou_decimal = 'inteiro'
    else:
        inteiro_ou_decimal = 'decimal'
    if inteiro_ou_decimal == 'inteiro':
       if operação == 0:
          par_ou_ímpar = 'Neutro'
       elif operação%2 == 0:
          par_ou_ímpar = 'par'
       else:
         par_ou_ímpar = 'ímpar'
    else: 
        par_ou_ímpar = 'não é par e nem ímpar pelo fato de ser decimal'
    if operação < 0:
        positivo_negativo = 'negativo'
    else:
        positivo_negativo = 'positivo'
    Certo = True


elif operação == 'Divisão':
    operação = numero1 / numero2
    inteiro = int(operação)
    if inteiro == operação:
        inteiro_ou_decimal = 'inteiro'
    else:
        inteiro_ou_decimal = 'decimal'
    if inteiro_ou_decimal == 'inteiro':
       if operação == 0:
          par_ou_ímpar = 'Neutro'
       elif operação%2 == 0:
          par_ou_ímpar = 'par'
       else:
         par_ou_ímpar = 'ímpar'
    else: 
        par_ou_ímpar = 'não é par e nem ímpar pelo fato de ser decimal'
    if operação < 0:
        positivo_negativo = 'negativo'
    else:
        positivo_negativo = 'positivo'
    Certo = True

elif operação == 'Subtração':
    operação = numero1 - numero2
    inteiro = int(operação)
    if inteiro == operação:
        inteiro_ou_decimal = 'inteiro'
    else:
        inteiro_ou_decimal = 'decimal'
    if inteiro_ou_decimal == 'inteiro':
       if operação == 0:
          par_ou_ímpar = 'Neutro'
       elif operação%2 == 0:
          par_ou_ímpar = 'par'
       else:
         par_ou_ímpar = 'ímpar'
    else: 
        par_ou_ímpar = 'não é par e nem ímpar pelo fato de ser decimal'
    if operação < 0:
        positivo_negativo = 'negativo'
    else:
        positivo_negativo = 'positivo'
    Certo = True

elif operação == 'Multiplicação':
    operação = numero1 * numero2
    inteiro = int(operação)
    if inteiro == operação:
        inteiro_ou_decimal = 'inteiro'
    else:
        inteiro_ou_decimal = 'decimal'
    if inteiro_ou_decimal == 'inteiro':
       if operação == 0:
          par_ou_ímpar = 'Neutro'
       elif operação%2 == 0:
          par_ou_ímpar = 'par'
       else:
         par_ou_ímpar = 'ímpar'
    else: 
        par_ou_ímpar = 'não é par e nem ímpar pelo fato de ser decimal'
    if operação < 0:
        positivo_negativo = 'negativo'
    else:
        positivo_negativo = 'positivo'
    Certo = True
if Certo:
    print(f'O resultado é {operação}, {par_ou_ímpar}, {positivo_negativo} e {inteiro_ou_decimal}.')
else:
    print(f'Erro! "{operação}" não é uma operação válida!')