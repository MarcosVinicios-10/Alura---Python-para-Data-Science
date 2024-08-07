'''
12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Copiar código
Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
'''
pesquisa = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

maior = max(pesquisa.values())
for e in pesquisa:
    if pesquisa[e] == maior:
        print(f'O desing mais votado foi o: "{e}".')
        print(f'Representando {(maior*100)/sum(pesquisa.values()):.2f}% dos votos')