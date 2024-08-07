'''
11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
'''
m1 = float(input('Digite um lado do triângulo: '))
m2 = float(input('Digite um lado do triângulo: '))
m3 = float(input('Digite um lado do triângulo: '))

if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    if m1 == m2 == m3:
        print('É possível formar um triângulo, e ele será equilátero')
    elif m1 == m2 or m1 == m3 or m2 == m3:
        print('É possível formar um triângulo, e ele será isóceles.')        
    else:
        print('É possível formar um triângulo, e ele será escaleno.')        
else:
    print('Não é possível formar um triângulo.')
