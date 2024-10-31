def permutar(array, R, permutacion_actual=[], usadas=[]):
    # Caso base: si la permutación actual tiene el tamaño R, se imprime
    if len(permutacion_actual) == R:
        print(permutacion_actual)
        return
    
    #se recorrenlos elementos del arreglo
    for i in range(len(array)):
        # Si el elemento no ha sido usado en la permutación actual, se añade
        if i not in usadas:
            # Añadir el elemento a la permutación actual
            permutacion_actual.append(array[i])
            usadas.append(i)
            
            # Llamada recursiva para generar permutaciones
            permutar(array, R, permutacion_actual, usadas)
            
            # Deshacer el cambio
            #se usa backtracking pyues se deshace el cambio
            permutacion_actual.pop()
            usadas.pop()


array = [1, 2, 3, 4]
R = 2,4

permutar(array, R)
