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
# Dividir para conquistar
# O Merge Sort, inicialmente calcula o ponto médio do sub-arranjo, o que demora um tempo constante, logo depois resolve dois subproblemas, recursivamente, cada um de tamanho n/2, o que acabada contribuindo 2T(n/2) para o tempo de execução. Depois ele uni os sub arranjos em um único conjunto ordenado.
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
