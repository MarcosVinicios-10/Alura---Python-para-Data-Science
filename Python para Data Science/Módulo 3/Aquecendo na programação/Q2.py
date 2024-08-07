# 2. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

porcentagem = float(input("Qual a porcentagem de crescimento da produção da empresa? "))

if porcentagem > 0:
    print(f'Houve um cresciemnto de {porcentagem}%.')
elif porcentagem == 0:
    print(f'Não houve crescimento.')
else:
    print(f'Houve um decrescimo de {porcentagem}%.')
