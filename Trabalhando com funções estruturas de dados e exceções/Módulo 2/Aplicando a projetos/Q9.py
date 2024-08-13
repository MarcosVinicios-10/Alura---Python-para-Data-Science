'''
9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para uma das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer 
em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os 
gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"
'''
                             # Hotel, Gastos Diários, DIstância e Preço do combústivél 
gastos_viagem = {'Salvador': [150,200,850], 'Fortaleza': [150,400,800], "Natal": [150,250,300], 'Aracaju': [150,300,550]}
autonomia = 14

def gasto_hotel(x):
    for valores in x.values():
        hotel = valores[0]*3
        valores.append(hotel)

def gasto_gasolina(x):
    for valores in x.values():
        combustivel = ((valores[2]/14) * 5) * 2
        valores[-1] = valores[-1] + combustivel
gasto_gasolina(gastos_viagem)

def gasto_passeio(x):
    for valores in x.values():
        diário = valores[1] * 3
        valores[-1] = valores[-1] + diário
gasto_passeio(gastos_viagem)

for cidade, valores in gastos_viagem.items():
    print(f"Com base nos gastos definidos, uma viagem de 3 dias para {cidade} saindo de Recife custaria R${valores[-1]:,.2f} reais")