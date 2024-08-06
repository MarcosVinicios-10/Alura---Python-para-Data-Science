# 5 Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

primos = []
limite = int(input('Insira um número: '))

for a in range(2,limite):
    for e in range(2,limite):
        if a == 2:
            primos.append(a)
            break
        elif a%e == 0:
            break
        elif e == a -1:
            primos.append(a)
print(primos)