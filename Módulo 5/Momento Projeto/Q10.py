'''
10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, 
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
'''
média_mensal = []
mês = []
for e in range(1,13):
    a = input('Insira o mês: ')
    temperatura = float(input('Insira a média da temperatura: '))
    média_mensal.append(temperatura)
    mês.append(a)
médial_anual = sum(média_mensal)/12
print(f'A média anual foi de: {médial_anual}')
for e in range(0,12):
    if média_mensal[e] > médial_anual:
        print(f'A temperatura foi maior no mês {mês[e]}, {média_mensal[e]}°')
