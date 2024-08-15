'''
7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. 
O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação 
para definir a melhor condição para os testes.

Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e 
gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:

Dados sem exceção:
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

Dados com exceção:
1) Exceção de ZeroDivisionError

pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

2) Exceção de ValueError

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]
'''
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

def divide_coluna(pressão,temp):
    try:
        if len(pressão) != len(temp):
            raise ValueError
        elif 0 in temp:
            raise ZeroDivisionError
    except ValueError:
        print(f'{ValueError} O tamanho das listas são diferentes.')
    except ZeroDivisionError:
        print(f'{ZeroDivisionError} Existe uma divisão por zero.')
    else:
        razão = [list(map(lambda x,y: x/y ,pressão,temp))]
        return razão
print(divide_coluna(pressoes,temperaturas))