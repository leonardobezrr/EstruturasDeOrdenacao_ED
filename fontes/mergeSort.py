lista = [3,5,2,20,1,50,30,4]

def mergeSort(lista):
    # Condição de parada: se a lista tem apenas um elemento, ela já está ordenada
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Ordena recursivamente as sublistas esquerda e direita
    esquerda = mergeSort(esquerda)
    direita = mergeSort(direita)

    return merge(esquerda, direita)


def merge(esquerda, direita):
    listaOrdenada = []
    i = 0  # índice para percorrer a lista esquerda
    j = 0  # índice para percorrer a lista direita

    # Combina as sublistas ordenadas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            listaOrdenada.append(esquerda[i])
            i += 1
        else:
            listaOrdenada.append(direita[j])
            j += 1

    # Adiciona os elementos restantes, se houver, de uma das sublistas
    listaOrdenada.extend(esquerda[i:])
    listaOrdenada.extend(direita[j:])

    return listaOrdenada

print("Lista Desordenada: ",lista)
print()
print("Lista Ordenada: ", mergeSort(lista))
