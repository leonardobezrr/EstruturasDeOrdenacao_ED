import time
from insertionSort import insertionSort
from distributionSort import distributionSort
from mergeSort import mergeSort
from quickSort import quickSort
from selectionSort import selectionSort
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

#INSERTION SORT
lista = [3, 2, 1, 5, 4]
for i in range (100,900):
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
for i in range (100,900):
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
for i in range (100,900):
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
for i in range (100,900):
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
for i in range (100,900):
    tempo = calcular_tempo_execucao(selectionSort, lista)
    tempoEmMicroS = tempo * 10**6
    v_selection.append(tempoEmMicroS)

print("Quick Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresSelection.txt", "w") as valoresSelection:
    for tempo in v_selection:
        valoresSelection.write("%.6f\n" % tempo)

print("valores salvos no arquivo 'valoresSelection.txt'.")
print()
