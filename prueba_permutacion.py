# Author: Javier Montoya Perez
# Date: 31/10/2024 

def generar_permutaciones(array, R):
    resultado = []

    def backtrack(permutacion_actual, usadas):
        # Caso base: si la permutación actual tiene tamaño R, 
        #se guarda en el resultado
        if len(permutacion_actual) == R:
            resultado.append(permutacion_actual[:])  # Copiamos la permutación
            return                                                                                                          

        # se recorre el array para agregar elementos a la lista de permutación
        for i in range(len(array)):
            if i not in usadas:  # Verifica que el elemento no se haya usado
                permutacion_actual.append(array[i])
                usadas.add(i)
                
                # Llamada recursiva para continuar construyendo la lista de permutación
                backtrack(permutacion_actual, usadas)
                
                # aqui se aplica backtracking
                permutacion_actual.pop()
                usadas.remove(i)

    # función recursiva
    backtrack([], set())
    
    # ordenando el resultado con sort

    resultado.sort()
    
    for perm in resultado:
        print(' '.join(map(str, perm)))


# Entrada de datos
# Entrada de datos
#N, R = map(int, input("Introduce N y R separados por espacio: ").split())  # Ej. 4 2
#array = list(map(int, input("Introduce los elementos del arreglo separados por espacio: ").split()))  # Ej. 1 2 3 4

inp = input()
parameters = inp.split()

N = int(parameters[0])
R = int(parameters[1])

# Generamos las permutaciones de tamaño R
generar_permutaciones(parameters, R)
