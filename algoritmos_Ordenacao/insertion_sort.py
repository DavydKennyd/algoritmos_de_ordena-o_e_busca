### ORDENAÇÃO EM INSERTION SOR

def insertion_sort(array):
    
    for i in range(1,len(array)):

        elemento = array[i]
        j = i-1

        while j >= 0 and array[j] > elemento:
            array[j + 1] = array[j]
            j -= 1 

        array[j +1] = elemento

    return array

lista = [5, 2, 8, 3, 1, 6, 4]
lista_ordenada = insertion_sort(lista)
print(lista_ordenada)  

### A SAÍDA DEVE SER A SEGUINTE ----> [1, 2, 3, 4, 5, 6, 8]