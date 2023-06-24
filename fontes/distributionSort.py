import random
def gerar_array_aleatorio(tamanho):
    array_aleatorio = []
    for _ in range(tamanho):
        valor_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        array_aleatorio.append(valor_aleatorio)
    return array_aleatorio

# Exemplo de uso
tamanho_do_array = 100
lista = gerar_array_aleatorio(tamanho_do_array)
def distributionSort(lista):
    # Encontra o valor máximo no lista
    maxValue = max(lista)
    if isinstance(maxValue, float):
        maxValue = int(maxValue)

    countLista = [0] * (maxValue + 1)
    # Cria um lista com zeros com tamanho do valor máximo + 1

    for i in lista:
        index = int(i)
        countLista[index] += 1


    listaOrdenada = []
    # Preenche o listaOrdenada com os elementos ordenados
    for i in range(maxValue + 1):
        for j in range(countLista[i]):
            listaOrdenada.append(i)
    return listaOrdenada

print("Lista Desordenada: ",lista)
print()
print("Lista Ordenada: ", distributionSort(lista))

