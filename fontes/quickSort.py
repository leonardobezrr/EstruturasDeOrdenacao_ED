lista = [3,5,2,20,1,50,30]
#O método de ordenação quick sort funciona da seguinte maneira: Um elemento da lista, é denomidado pivô, posteriormente a lista é rearranjada de forma que todos os elementos anteriores ao pivô sejam menores que ele, e todos os elementos posteriores ao pivô sejam maiores que ele. Ao fim do processo o pivô estará em sua posição final e haverá duas sub listas não ordenadas. Depois, recursivamente, a sub lista dos elementos menores são ordenadas assim como a sub lista dos elementos maiores
def quickSort(lista):
    if len(lista) <= 1:
        return lista 
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


