import time
from insertionSort import insertionSort
from distributionSort import distributionSort
from mergeSort import mergeSort
from quickSort import quickSort
from selectionSort import selectionSort
import random
import os 
os.system("cls")
v_insertion=[]
v_distribution=[]
v_merge = []
v_quick = []
v_selection = []
def gerar_lista_aleatoria(tamanho):
    lista_aleatoria = []
    valor_anterior = 100
    for _ in range(tamanho):
        limite_superior = valor_anterior - 1
        limite_inferior = limite_superior - 10
        valor_aleatorio = random.randrange(limite_inferior, limite_superior)  # Gera um número aleatório entre valor_anterior + 1 e 100
        lista_aleatoria.append(valor_aleatorio)
        valor_anterior = valor_aleatorio
    return lista_aleatoria
# O insertion sort vai percorrer o vetor e caso o elemento anterior for menor ele troca de posição, vai repetindo esse processo até o vetor estar ordenado
# É útil para pequenas entradas 
# Melhor caso - Linear;
#Médio e pior caso - Quadrático;

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

# Defina o tamanho máximo da lista e o incremento desejado
tamanho_maximo = 1000
incremento = 100

tempos = []
tamanhos = []

# Realize a ordenação para diferentes tamanhos de lista
for tamanho in range(incremento, tamanho_maximo + 1, incremento):
    lista = gerar_lista_aleatoria(tamanho)

    # Calcule o tempo de execução
    start_time = time.time()
    insertionSort(lista)
    end_time = time.time()
    tempo_execucao = end_time - start_time

    # Armazene os tempos e tamanhos para plotagem
    tempos.append(tempo_execucao)
    tamanhos.append(tamanho)

# Salve os resultados em um arquivo de texto
with open("valoresInsertion_pior.txt", "w") as arquivo:
    for i in range(len(tempos)):
        arquivo.write(f"{tamanhos[i]}\t{tempos[i]}\n")

