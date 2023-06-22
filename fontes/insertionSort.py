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
# O insertion sort vai percorrer o vetor e caso o elemento anterior for menor ele troca de posição, vai repetindo esse processo até o vetor estar ordenado
# É útil para pequenas entradas 
# Melhor caso: O(n), quando a matriz está ordenado; 
# Médio caso:
# Pior caso: O(n²), quando a matriz está em ordem inversa, daquela que deseja ordenar.

def insertionSort(lista):
    for i in range(1, len(lista)):
        eleAtual = lista[i]
        j = i - 1
        # enquanto o elemento anterior for maior que o valor atual e ainda houver elementos para iterar
        while j >= 0 and lista[j] > eleAtual:
            # move o elemento anterior para a próxima posição na lista
            lista[j + 1] = lista[j]
            # atualiza a posição do elemento anterior para o próximo elemento
            j -= 1
        # insere o valor atual na posição correta na lista
        lista[j + 1] = eleAtual
    return lista
print("Lista Desordenada: ",lista)
print()
insertionSort(lista)
print("Lista Ordenada: ",lista)
