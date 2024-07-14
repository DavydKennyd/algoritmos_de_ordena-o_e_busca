#### ORDENAÇÃO DA SHELL SORT 

def shell_sort(lista):
    gap = len(lista) // 2  ##### A VARIÁVEL É GAP PORQUE O ALGORITMO SHELL SORT É UMA VARIAÇÃO DO INSERTION SORT QUE USA UMA TÉCNICA CHAMADA "GAP" PARA ORDENAR A LISTA.

    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i  ### INICIALIZA J COMO I

            ##### MOVE OS ELEMENTOS QUE ESTÃO GAP POSIÇÕES À FRENTE ATÉ A POSIÇÃO CORRETA
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            lista[j] = temp  #### INSERE O ELEMENTO NA POSIÇÃO CORRETA

        gap //= 2  #### REDUZ O GAP

    return lista

#### TESTANDO O CÓDIGO
lista_para_teste = [3, 6, 8, 10, 1, 3, 2, 1, 2, 5]
lista_ordenada = shell_sort(lista_para_teste)
print(lista_ordenada)

#### O RESULTADO DEVE SER A SEGUINTE SAÍDA ---> [1, 1, 2, 2, 3, 3, 5, 6, 8, 10]