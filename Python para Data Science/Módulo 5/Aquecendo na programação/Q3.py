# 3 Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

lista = []
x = 0
while x < 5:
    a = int(input('Insira um número: ')) 
    lista.append(a)
    x+=1
print(lista)
