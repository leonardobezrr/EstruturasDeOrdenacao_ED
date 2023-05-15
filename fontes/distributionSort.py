lista = [3,5,2,20,1,50,30,4]

def distribution_sort(lista):
    # Encontra o valor máximo no lista
    maxValue = max(lista)
    # Cria um lista com zeros com tamanho do valor máximo + 1
    countLista = [0] * (maxValue + 1)

    for i in lista:
        countLista[i] += 1

    listaOrdenada = []
    # Preenche o listaOrdenada com os elementos ordenados
    for i in range(maxValue + 1):
        for j in range(countLista[i]):
            listaOrdenada.append(i)
    return listaOrdenada

print("Lista Desordenada: ",lista)
print()
print("Lista Ordenada: ", distribution_sort(lista))

