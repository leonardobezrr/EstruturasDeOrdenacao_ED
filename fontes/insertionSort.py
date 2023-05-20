lista = [1,5,3,20,2,50,30]
# O insertion sort vai percorrer o vetor e caso o elemento anterior for menor ele troca de posição, vai repetindo esse processo até o vetor estar ordenado
# É útil para pequenas entradas 
# Melhor caso: O(n), quando a matriz está ordenado; 
# Médio caso: O(n²/4), quando a matriz tem valores aleatórios sem ordem de classificação (crescente ou decrescente);
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
