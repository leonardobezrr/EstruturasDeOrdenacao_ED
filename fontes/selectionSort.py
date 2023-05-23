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
