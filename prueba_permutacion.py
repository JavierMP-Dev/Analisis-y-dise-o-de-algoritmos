def permutar(array, R, permutacion_actual=[], usadas=[]):
    # Caso base: si la permutación actual tiene el tamaño R, se imprime
    if len(permutacion_actual) == R:
        print(permutacion_actual)
        return
    
    # Recorremos los elementos del array
    for i in range(len(array)):
        # Si el elemento no ha sido usado en la permutación actual, lo añadimos
        if i not in usadas:
            # Añadir el elemento a la permutación actual
            permutacion_actual.append(array[i])
            usadas.append(i)
            
            # Llamada recursiva para continuar generando permutaciones
            permutar(array, R, permutacion_actual, usadas)
            
            # Deshacer el cambio (backtracking)
            permutacion_actual.pop()
            usadas.pop()

# Ejemplo de uso:
array = [1, 2, 3, 4]
R = 2
permutar(array, R)
