'''
7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus 
nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"
Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
nomes_formatado = []

def tratamento_nomes(x,y):
    for a,b in zip(x,y):
      a = a.lower().capitalize()
      b = b.lower().capitalize().rjust(len(b)+1)
      nomes_formatado.append((a) + (b))

tratamento_nomes(nomes,sobrenomes)
for i in nomes_formatado:
   print(f'Nome completo: {i}.')