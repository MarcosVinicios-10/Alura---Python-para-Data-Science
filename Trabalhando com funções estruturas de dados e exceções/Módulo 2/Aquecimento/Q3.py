'''
3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.
'''

numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
múltiplos = []

def multiplos(x):
    for i in x:
        if i%3 == 0:
         múltiplos.append(i)
    return múltiplos

print(multiplos(numeros))
