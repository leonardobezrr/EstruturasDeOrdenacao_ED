lista = [1,5,3,20,2,50,30]

def insertion_sort(lista):
    # itera sobre cada elemento na lista a partir do segundo elemento
    for i in range(1, len(lista)):
        # armazena o valor do elemento atual em uma variável temporária
        eleAtual = lista[i]
        # armazena a posição do elemento anterior na lista
        j = i - 1
        # enquanto o elemento anterior for maior que o valor atual e ainda houver elementos para iterar
        while j >= 0 and lista[j] > eleAtual:
            # move o elemento anterior para a próxima posição na lista
            lista[j + 1] = lista[j]
            # atualiza a posição do elemento anterior para o próximo elemento
            j -= 1
        # insere o valor atual na posição correta na lista
        lista[j + 1] = eleAtual
    # retorna a lista ordenada
    return lista

print("Lista Desordenada: ",lista)
print()
insertion_sort(lista)
print("Lista Ordenada: ",lista)
