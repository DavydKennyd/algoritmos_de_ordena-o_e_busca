### BUSCA SEQUENCIAL

def busca_sequencial(array, num_acha):
    
    ###VOU COMEÇAR PELO PRIMEIRO ELEMENTO E IR ATÉ O ÚLTIMO.
    for i in range(len(array)):
        ##SE O ELEMENTO ATUAL FOR IGUAL AO `num_acha`, EU ENCONTREI!
        if array[i] == num_acha:
            return i  ##RETORNO O ÍNDICE DO ELEMENTO ENCONTRADO
    
    ###SE EU NÃO ENCONTRAR O ELEMENTO, RETORNO -1.
    return -1

lista = [5, 2, 8, 3, 1, 6, 4]
bucsa = busca_sequencial(lista, 3)
print(bucsa)  # 3

index = busca_sequencial(lista, 10)
print(bucsa)  ### (VAI APARECER -1 SE O NUMERO NÃO FOR ENCONTRADO)

##A SAÍDA DEVE SER ESSA --->>> 3