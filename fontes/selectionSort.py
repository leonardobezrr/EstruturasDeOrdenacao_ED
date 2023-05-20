import numpy as np
from PyGnuplot import gp
lista = [1,5,3,20,2,50,30]

# A complexidade deste algoritmo será sempre O(n²);
#O algoritmo selection sort não necessita de um vetor auxiliar ;
#O selection sort compara a cada interação um elemento com os outros,  visando encontrar o menor. Dessa forma, podemos entender que não  existe um melhor caso mesmo que o vetor esteja ordenado ou em ordem  inversa serão executados os dois laços do algoritmo, o externo e o interno.
def selectionSort(lista):
    n = len(lista)
    for i in range(n):
        # Encontrando o menor elemento restante na lista desordenada
        menor = i
        for j in range(i+1, n):
            if lista[j] < lista[menor]:
                menor = j
        # Trocando o menor elemento encontrado com o primeiro elemento restante na lista desordenada
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
print("Lista Desordenada: ",lista)
print()
selectionSort(lista)
print("Lista Ordenada: ",lista)
