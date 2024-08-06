# 2 Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

lista =  [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
x = 0
acima_3000 = 0
for e in lista:
    if e > 3000:
        acima_3000+=e
        x+=1
print(f'Foram feitas um total de {x} compras acima de R$ 3.000,00. Sendo {(acima_3000*100)/(sum(lista)):.2f}% do total de compras.')