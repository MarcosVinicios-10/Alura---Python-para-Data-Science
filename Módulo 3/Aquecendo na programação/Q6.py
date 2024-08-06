# 6 Escreva um programa que leia três números e os exiba em ordem decrescente.
# AQUI
numero1 = float(input('Qual o primeiro número: '))
numero2 = float(input('Qual o segundo número: '))
numero3 = float(input('Qual o terceiro número: '))
x = 0
z = 0
if numero1 >= numero2 and numero1 >= numero3:
    print(numero1)
    if numero2 > numero3:
       print(numero2)
       menor = numero3
    else:
      print(numero3)
      menor = numero2 

if numero2 >= numero3 and numero2 > numero1:
  print(numero2)
  if numero1 > numero3:
    print(numero1)
    menor = numero3
  else: 
    print(numero3)
    menor = numero1

if numero3 > numero1 and numero3 > numero2:
    print(numero3)
    if numero1 > numero2:
      print(numero1)
      menor = numero2
    else:
      print(numero2)
      menor = numero1
     

print(menor)

