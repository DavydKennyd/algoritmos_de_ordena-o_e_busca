##FUNCÕES RECURSIVAS EM FIBONACCI


def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)


### ESSE FOR SERVE PARA TESTAR A FUNÇÃO COM DIFERENTES NUMEROS QUE NO CASO SERIA O N
for i in range(5): ## TESTANDO PRIMEIROS NUMEROS DA SEQUENCIA DE FIBONACCI
    print(f"Fibonacci({i}) = {fibonacci(i)}") 

### A SAÍDA DEVE SER A SEGUINTE
###Fibonacci(1) = 1
###Fibonacci(2) = 1
###Fibonacci(3) = 2
###Fibonacci(4) = 3