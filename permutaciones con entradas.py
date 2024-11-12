# Author: Javier Montoya Perez
# Date: 31/10/2024 
# Entrada de datos
inp = input()
parameters = inp.split()
N = int(parameters[0])
R = int(parameters[1])

# Lectura de los elementos del arreglo
array = list(map(int, input().split()))

def generar_permutaciones(arr, r):
    resultado = []

    # Función recursiva para generar permutaciones
    def backtrack(permutacion_actual, usadas):
        if len(permutacion_actual) == r:
            resultado.append(permutacion_actual[:])
            return
        for i in range(len(arr)):
            if i not in usadas:
                usadas.add(i)
                permutacion_actual.append(arr[i])
                backtrack(permutacion_actual, usadas)
                permutacion_actual.pop()
                usadas.remove(i)

    # Llamada inicial
    backtrack([], set())

    # Mostrar resultado
    for perm in resultado:
        print(" ".join(map(str, perm)))

# Llamada a la función con los datos de entrada
generar_permutaciones(array, R)
