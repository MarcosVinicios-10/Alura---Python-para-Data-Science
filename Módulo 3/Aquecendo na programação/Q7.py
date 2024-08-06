# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = input("Qual turno você estuda? Manhã, Tarde ou Noite?")

if turno == 'Manhã':
    print('Bom dia!')
elif turno == 'Noite':
    print('Boa noite!')
elif turno == 'Tarde':
    print('Boa tarde!')
else:
    print('Mensagem inválida.')