import time

start_time = time.perf_counter()

def permutar_recursivo(pares, permutaciones, actual=[]):
    # Si hemos llegado a una permutación completa
    if not pares:
        permutaciones.append(actual)
        return

    # Iterar sobre los pares restantes
    for i, par in enumerate(pares):
        # Construir una nueva permutación con el par actual
        nueva_permutacion = actual + [par]
        # Llamar a la función recursiva con los pares restantes
        permutar_recursivo(pares[:i] + pares[i+1:], permutaciones, nueva_permutacion)

def permutar_listas(lista1, lista2):
    # Combinar los elementos de ambas listas en pares de 2 en 2
    pares = list(zip(lista1, lista2))
    permutaciones = []
    permutar_recursivo(pares, permutaciones)
    return permutaciones

# Ejemplo de uso
lista1 = [5, 6]
lista2 = [1, 2,3,4]
resultado = permutar_listas(lista1, lista2)

for p in resultado:
    print(p)

end_time = time.perf_counter()
print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")