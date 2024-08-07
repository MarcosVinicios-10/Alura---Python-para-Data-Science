'''
13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão.
O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
'''
vendas_2022 = int(input('Quantidade de vendas em 2022: '))
vendas_2023 = int(input('Quantidade de vendas em 2023: '))

if vendas_2022 > vendas_2023:
  variação = ((vendas_2023 - vendas_2022)/vendas_2022*100)
else:
  variação = ((vendas_2023 - vendas_2022)/vendas_2022*100)

if variação > 20:
  print('Bonificação para o time de vendas.')
elif 20 > variação and variação > 2:
  print('Pequena bonificação para o time de vendas.')
elif 2 >= variação and variação >= -10:
  print('Planejamento de políticas de incentivo às vendas.')
else:
  print('Corte de gastos.')
