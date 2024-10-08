'''
15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
'''

idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
          'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
          'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
          'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
média_geral =0
for setor, dados in idades.items():
    média = sum(dados)/len(dados)
    média_geral += sum(dados)
    print(f'A média de idades do {setor} é {média:,.2f}')

média_geral = média_geral/40
x = 0

for dados in idades.values():
    for idade in dados:
      if idade > média_geral:
         x +=1 

print(f'A média geral é {média_geral}. {x} pessoas estão acima da média geral.')