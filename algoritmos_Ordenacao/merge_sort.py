#### ORDENAÇÃO EM MERGE SORT 
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    while len(esquerda) > 0 and len(direita) > 0:
        if esquerda[0] <= direita[0]:
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))
    resultado.extend(esquerda)
    resultado.extend(direita)
    return resultado

# DEFININDO A LISTA PARA TESTAR 
lista_para_teste = [3, 6, 8, 10, 1, 3, 2, 1, 2, 5]

resultado = merge_sort(lista_para_teste)
print(resultado)

### O RESULTADO DE SAÍDA DEVE SER ESSA DAQUI ---> [1, 1, 2, 2, 3, 3, 5, 6, 8, 10]