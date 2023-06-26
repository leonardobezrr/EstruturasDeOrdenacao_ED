import time
from insertionSort import insertionSort
from distributionSort import distributionSort
from mergeSort import mergeSort
#from quickSort import quickSort
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
        limite_superior = 100
        limite_inferior = 1
        valor_aleatorio = random.randint(limite_inferior, limite_superior)  # Gera um número aleatório entre valor_anterior + 1 e 100
        lista_aleatoria.append(valor_aleatorio)
        valor_anterior = valor_aleatorio
    return lista_aleatoria
# O insertion sort vai percorrer o vetor e caso o elemento anterior for menor ele troca de posição, vai repetindo esse processo até o vetor estar ordenado
# É útil para pequenas entradas 
# Melhor caso - Linear;
#Médio e pior caso - Quadrático;

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
    selectionSort(lista)
    end_time = time.time()
    tempo_execucao = end_time - start_time

    # Armazene os tempos e tamanhos para plotagem
    tempos.append(tempo_execucao)
    tamanhos.append(tamanho)

# Salve os resultados em um arquivo de texto
with open("valoresSelection.txt", "w") as arquivo:
    for i in range(len(tempos)):
        arquivo.write(f"{tamanhos[i]}\t{tempos[i]}\n")

