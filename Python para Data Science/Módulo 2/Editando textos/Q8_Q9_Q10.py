'''
8. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
9. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''
frase = input('Digite uma frase: ')
print(f'Está é sua frase com todos as vógais "e" trocados por "f": {frase.replace("e","f")}')
print(f'Está é sua frase com todos as vógais "a" trocados por "@": {frase.replace("a","@")}')
print(f'Está é sua frase com todos as vógais "s" trocados por "$": {frase.replace("s","$")}')
print(f'Tudo misturado: {frase.replace("e","f").replace("a","@").replace("s","$")}')
