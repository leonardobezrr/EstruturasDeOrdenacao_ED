import time
from insertionSort import insertionSort
import os 
os.system("cls")
v=[]

def calcular_tempo_execucao(algoritmo, teste):
    inicio = time.perf_counter()
    algoritmo(teste)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    return tempo_execucao

lista = [3, 2, 1, 5, 4]
for i in range (100,900):
    tempo = calcular_tempo_execucao(insertionSort, lista)
    tempoEmMicroS = tempo * 10**6
    v.append(tempoEmMicroS)

print("Insertion Sort")
print("Tempo de execução: %.3f µs"%tempoEmMicroS)

with open("valoresInsertion.txt", "w") as valoresInsertion:
    for tempo in v:
        valoresInsertion.write("%.6f\n" % tempo)

print("Valores salvos no arquivo 'valoresInsertion.txt'.")