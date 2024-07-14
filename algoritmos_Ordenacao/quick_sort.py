### ORDENAÇÃO EM QUICK_SORT

def quick_sort(lista):
    if len(lista) < 1:
        return lista

    pivo = lista[0]

    n_menores = [x for x in lista[1:] if x < pivo]
    n_maiores = [x for x in lista[1:] if x > pivo]

    return quick_sort(n_menores) + [pivo] + quick_sort(n_maiores)

# Definindo a lista para testar
lista_para_testar = [3, 6, 8, 10, 1, 2, 1]

#### TESTANDO A FUNÇÃO COM A LISTA DEFINIDA JÁ
lista_ordenada = quick_sort(lista_para_testar)
print(lista_ordenada)


###A SAÍDA DEVE SER A SEGUINTE --->> [1, 2, 3, 6, 8, 10]