'''
3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a 
posição do nome na lista original e o segundo elemento sendo o próprio nome.
'''

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

posição_lista=[]
for nome in lista:
    posição_lista.append((lista.index(nome), nome))
print(posição_lista)
