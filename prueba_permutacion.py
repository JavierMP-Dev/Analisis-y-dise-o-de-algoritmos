# Author: Javier Montoya Perez
# Date: 31/10/2024 

def generar_permutaciones(array, R):
    resultado = []

    def backtrack(permutacion_actual, usadas):
        # Caso base: si la permutación actual tiene tamaño R, la guardamos en el resultado
        if len(permutacion_actual) == R:
            resultado.append(permutacion_actual[:])  # Copiamos la permutación
            return                                                                                                          

        # Recorremos el array para agregar elementos a la permutación
        for i in range(len(array)):
            if i not in usadas:  # Verificamos que el elemento no se haya usado
                permutacion_actual.append(array[i])
                usadas.add(i)
                
                # Llamada recursiva para continuar construyendo la permutación
                backtrack(permutacion_actual, usadas)
                
                # Deshacemos el cambio (backtracking)
                permutacion_actual.pop()
                usadas.remove(i)

    # Llamamos a la función recursiva
    backtrack([], set())
    
    # Ordenamos el resultado y lo imprimimos
    resultado.sort()
    for perm in resultado:
        print(' '.join(map(str, perm)))


# Entrada de datos
# Entrada de datos
N, R = map(int, input("Introduce N y R separados por espacio: ").split())  # Ej. 4 2
array = list(map(int, input("Introduce los elementos del arreglo separados por espacio: ").split()))  # Ej. 1 2 3 4


# Generamos las permutaciones de tamaño R
generar_permutaciones(array, R)
