lista = [3,5,2,20,1,50,30]

def quickSort(lista):
    if len(lista) <= 1:
        return lista #Caso a lista tenha tamanho menor ou igual a 1
    else:
        pivo = lista[0] # Seleciona o pivo como o primeiro elemento da lista
        esquerda = []
        direita = []
        for i in range(1, len(lista)): # Vai percorrer de 1,6
            if lista[i] < pivo: #se for menor vai pra lista da esquerda
                esquerda.append(lista[i])
            else:
                direita.append(lista[i])#vai pra lista da direita 
        return quickSort(esquerda) + [pivo] + quickSort(direita)
    
print("Lista Desordenada: ",lista)
print()
print("Lista Ordenada: ", quickSort(lista))


