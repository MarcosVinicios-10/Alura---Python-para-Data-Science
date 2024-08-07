'''
7 Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado 
a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de 
bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
'''

bactérias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
lista_percentual = []
anterior = 0
dia = 1
for e in bactérias:
    if e == bactérias[0]:
        print(f'No dia {dia} tivemos {e} mil bactérias.')
        anterior = e
        dia +=1
        continue
    percentual = 100 * (e - anterior) / (anterior)
    print(f'Dia {dia}: {e} mil bactérias \tCreascimento percentual de {percentual:.2f}%')
    dia += 1
    anterior = e
    lista_percentual.append(percentual)
