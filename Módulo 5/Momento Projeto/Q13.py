'''
13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a 
verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão
o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o 
abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
'''

salarios = {1172 : 0, 1644: 0, 2617: 0, 5130: 0, 5532: 0, 6341: 0, 6650: 0, 7238: 0, 7685: 0, 7782: 0, 7903: 0}
x = 0

for e in salarios:
    abono = (e * 10) / 100
    if abono < 200:
        diferença = 200 - abono
        abono += diferença
        salarios[e] = abono
        x+=1
    else:
        salarios[e] = abono
print(f'{x} funcionários receberam o abono mínimo, o total de gastos com abono foi de R${sum(salarios.values()):,.2f} e o maior abono foi de R${max(salarios.values()):.2f}')
print(salarios)