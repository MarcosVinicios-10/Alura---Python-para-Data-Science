# 3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = input('Insira uma letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'"{letra}" é uma vogal!')
else:
    print(f'"{letra}" é uma consoante!')
