'''
4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo 
elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, 
a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.' Dados para testar a função:

Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]

Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]
'''
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

def JuntarListas(lista1,lista2) -> list:
    lista3 = []
    try:
        if not(len(lista1) == len(lista2)):
            raise IndexError
        for i,j in zip(lista1,lista2):
            lista3.append((i,j,i+j))
    except IndexError:
        print(f'Erro! {IndexError}')
    except Exception as e:
        print(f'Erro! {Exception} {e}')
    else:
        return lista3
lista3 = JuntarListas(lista1,lista2)
print(lista3)