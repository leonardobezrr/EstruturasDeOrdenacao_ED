
def distribution_sort(lista):
    # Encontra o valor máximo no lista
    max_value = max(lista)
    
    # Cria um lista com zeros com tamanho do valor máximo + 1
    count_lista = [0] * (max_value + 1)
    
    # Preenche o count_lista com a frequência de cada elemento no lista
    for i in lista:
        count_lista[i] += 1
        
    sorted_lista = []
    
    # Preenche o sorted_lista com os elementos ordenados
    for i in range(max_value + 1):
        for j in range(count_lista[i]):
            sorted_lista.append(i)
    
    return sorted_lista
