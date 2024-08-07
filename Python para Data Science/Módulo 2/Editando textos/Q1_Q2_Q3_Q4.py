'''
1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
2. Crie um código que solicite uma frase e depois imprima a frase na tela.
3. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
4. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
'''

frase = ("Bem-vindo(a)")
print(frase)
frase2 = input('Digite uma frase qualquer: ')
print(f'Está é sua frase "{frase2}"')
print(f'Está é sua frase com todas as letras maiúsculas: {frase2.upper()}')
print(f'Está é sua frase com todas as letras minúsculas: {frase2.lower()}')
