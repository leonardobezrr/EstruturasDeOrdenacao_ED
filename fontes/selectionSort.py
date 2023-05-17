import numpy as np
from PyGnuplot import gp

lista = [1,5,3,20,2,50,30]


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
