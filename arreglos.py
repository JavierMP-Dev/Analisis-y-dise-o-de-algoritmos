# Author: Javier Montoya Perez
# Date: 31/10/2024 
def permutar(array1, array2, R, permutacion_actual=[], usadas1=[], usadas2=[]):
    # Caso base: si la permutación actual tiene el tamaño R, se imprime
    if len(permutacion_actual) == R:
        # Imprimiendo la permutación actual sin corchetes ni comas, pero con un espacio que los separa
        print(' '.join(map(str, permutacion_actual)))
        return
    
    # Se recorren los elementos del primer arreglo
    for i in range(len(array1)):
        if i not in usadas1:
            # Añadir el elemento del primer arreglo a la permutación actual
            permutacion_actual.append(array1[i])
            usadas1.append(i)
            permutar(array1, array2, R, permutacion_actual, usadas1, usadas2)
            permutacion_actual.pop()
            usadas1.pop()  # Deshacer el uso de índices del primer arreglo

    # Se recorren los elementos del segundo arreglo
    for j in range(len(array2)):
        if j not in usadas2:
            # Añadir el elemento del segundo arreglo a la permutación actual
            permutacion_actual.append(array2[j])
            usadas2.append(j)
            permutar(array1, array2, R, permutacion_actual, usadas1, usadas2)
            permutacion_actual.pop()
            usadas2.pop()  # Deshacer el uso de índices del segundo arreglo

# Ejemplo de uso
array1 = [1, 2,3,4]
array2 = [4, 2]
R = 2  # Longitud de la permutación deseada
permutar(array1, array2, R)