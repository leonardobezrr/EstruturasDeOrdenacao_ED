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

def calcular_tempo_execucao(algoritmo, teste):
    inicio = time.perf_counter()
    algoritmo(teste)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    return tempo_execucao


#Valor aleatorio

def gerar_array_aleatorio(tamanho):
    array_aleatorio = []
    for _ in range(tamanho):
        valor_aleatorio = random.randint(1,100)  # Gera um número aleatório entre 1 e 1000
        array_aleatorio.append(valor_aleatorio)
    return array_aleatorio

# Exemplo de uso
tamanho_do_array = 100
lista = gerar_array_aleatorio(tamanho_do_array)



#INSERTION SORT
for i in range (1,10000,10):
    tempo = calcular_tempo_execucao(insertionSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_insertion.append(tempoEmMicroS)

print("Insertion Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresInsertion.txt", "w") as valoresInsertion:
    for tempo in v_insertion:
        valoresInsertion.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresInsertion.txt'.")
print()
#DISTRIBUTION SORT
for i in range (1,10000,10):
    tempo = calcular_tempo_execucao(distributionSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_distribution.append(tempoEmMicroS)

print("Distribution Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresDistribution.txt", "w") as valoresDistribution:
    for tempo in v_distribution:
        valoresDistribution.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresDistribution.txt'.")
print()

#MERGE SORT
for i in range (1,10000,10):
    tempo = calcular_tempo_execucao(mergeSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_merge.append(tempoEmMicroS)

print("Merge Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresMerge.txt", "w") as valoresMerge:
    for tempo in v_merge:
        valoresMerge.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresMerge.txt'.")
print()

#QUICK SORT
for i in range (1,10000,10):
    tempo = calcular_tempo_execucao(quickSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_quick.append(tempoEmMicroS)

print("Quick Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresQuick.txt", "w") as valoresQuick:
    for tempo in v_quick:
        valoresQuick.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresQuick.txt'.")
print()

#SELECTION SORT
for i in range (1,10000,10):
    tempo = calcular_tempo_execucao(selectionSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_selection.append(tempoEmMicroS)

print("Selection Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresSelection.txt", "w") as valoresSelection:
    for tempo in v_selection:
        valoresSelection.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresSelection.txt'.")
print()
