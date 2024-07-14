def busca_binaria(array, num_acha):
    baixo = 0
    alto = len(array) - 1
    
    while baixo <= alto:
        ### VOU CALCULAR O MEIO DO ARRAY.
        meio = (baixo + alto) // 2
        
        ### SE O ELEMENTO DO MEIO FOR IGUAL AO `NUM_ACHA`, EU ENCONTREI!
        if array[meio] == num_acha:
            return meio  ### RETORNO O ÍNDICE DO ELEMENTO ENCONTRADO
        
        ### SE O ELEMENTO DO MEIO FOR MENOR QUE O `NUM_ACHA`, EU PROCURO NA METADE DIREITA.
        elif array[meio] < num_acha:
            baixo = meio + 1
        
        # SE O ELEMENTO DO MEIO FOR MAIOR QUE O `NUM_ACHA`, EU PROCURO NA METADE ESQUERDA.
        else:
            alto = meio - 1
    
    
    return -1


lista = [1, 2, 3, 4, 5, 6, 8]

### TESTANDO A BUSCA BINÁRIA
busca = busca_binaria(lista, 3)
print(busca)  ### A SAÍDA DEVE SER 2

index = busca_binaria(lista, 10)
print(index)  ### DEVE APARECER -1 SE NÃO FOR ENCONTRADO 
