"""
1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
2. Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
"""

nome = input("Olá! Digite seu nome:")
idade = int(input("Agora sua idade:"))
altura = float(input("Por fim, sua altura:"))
print(f'Olá {nome}, você tem {idade} anos e mede {altura} metros!')

