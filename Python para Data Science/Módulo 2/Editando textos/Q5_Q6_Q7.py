'''
5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
6. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
7. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
'''

frase = " Está é uma frase sem espaços em branco no começo e no fim "
print(frase.strip())
frase2 = input("Escreva uma frase com espaços no início e no fim: ")
print(f'Está é sua frase: {frase2} ')
print(f'Está é sua frase sem espaços no início e no fim: {frase2.strip()}')
print(f'Está é sua frase sem espaços no início e no fim e com letras minúsculas: {frase2.strip().lower()}')
