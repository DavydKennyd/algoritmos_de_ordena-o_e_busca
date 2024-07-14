### ORDENAÇÃO COM BUBBLE SORT 

def bubble_sort(array):

    ### VOU COMEÇAR PELO PRIMEIRO ELEMENTO E COMPARÁ-LO COM OS ELEMENTOS ADJACENTES.
    for i in range(len(array)):
        ### VOU FAZER UMA PASSAGEM PELO ARRAY E TROCAR OS ELEMENTOS ADJACENTES SE NECESSÁRIO.
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

lista = [5, 2, 8, 3, 1, 6, 4]
lista_ordenado = bubble_sort(lista)
print(lista_ordenado)  


### A SAÍDA DEVE SER ESSA DAQUI ----> [1, 2, 3, 4, 5, 6, 8]