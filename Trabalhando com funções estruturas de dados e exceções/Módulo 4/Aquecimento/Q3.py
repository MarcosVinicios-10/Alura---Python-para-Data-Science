'''
3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro 
gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
'''
numbers = [3,4,6,76,12,33,44,99,88,2222,12,21,123,12,44,56,77.65,1,9,988]

def converteFloat(lista) -> list:
    try:
        for i in lista:
            if isinstance(i,int) or isinstance(i,float):
              None
            else:
                raise TypeError
    except TypeError:
        print(f'Erro! Tipo de erro: {TypeError}')
    else:
        for i in range(len(lista)):
            lista[i] = float(lista[i])
        return lista
            
    finally:
        print('Fim da execução da função.')
conversão=(converteFloat(numbers))
print(conversão)
