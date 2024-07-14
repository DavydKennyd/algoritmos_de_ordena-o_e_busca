### ORDENAÇÃO EM SELECTION SORT 
def selection_sort(array):
    # VOU COMEÇAR PELO PRIMEIRO ELEMENTO E ENCONTRAR O MENOR ELEMENTO DO RESTO DO ARRAY.
    for i in range(len(array)):
        # VOU ENCONTRAR O MENOR ELEMENTO DO RESTO DO ARRAY.
        menor_val = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor_val]:
                menor_val = j
        
        # VOU TROCAR O ELEMENTO ATUAL COM O MENOR ELEMENTO ENCONTRADO.
        array[i], array[menor_val] = array[menor_val], array[i]
    
    return array

lista = [5, 2, 8, 3, 1, 6, 4]
lista_ordenado = selection_sort(lista)
print(lista_ordenado) 

 ### A SAÍDA DEVE SER ESSA ---> [1, 2, 3, 4, 5, 6, 8]