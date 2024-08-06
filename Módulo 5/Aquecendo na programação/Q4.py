# 4 Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista = []
x = 0
while x < 5:
    a = int(input('Insira um número: ')) 
    lista.append(a)
    x+=1
lista.reverse()
print(lista)