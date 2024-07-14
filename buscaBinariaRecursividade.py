#### RERCUSIVIDADE EM BUSCA BINÁRIA

def busca_binaria(lista, elemento, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, fim)
    else:
        return busca_binaria(lista, elemento, inicio, meio - 1)

# A LISTA NÃO ORDENADA É ESSA (PODE ESCOLHER OUTRA LISTA SE PREFERIR)
lista = [1, 22, 43, 64, 15, 46, 71, 28, 19]

### SORT SERVE PARA ORDENAR A LISTA 
lista.sort()

### TESTANDO FUNÇÃO COM NUMEROS DIFERENTES
elementos_pra_teste = [8]

for elemento in elementos_pra_teste:
    resultado = busca_binaria(lista, elemento)
    print(f"busca_binaria({lista}, {elemento}) = {resultado}")
