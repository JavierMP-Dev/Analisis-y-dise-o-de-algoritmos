import time
start_time = time.perf_counter()

def permutar_recursivo(lista1, lista2, permutaciones, actual=[]):
    # Si ambas listas están vacías, hemos llegado a una permutación completa
    if not lista1 and not lista2:
        permutaciones.append(actual)
        return

    # Si todavía hay elementos en la lista1
    if lista1:
        permutar_recursivo(lista1[1:], lista2, permutaciones, actual + [lista1[0]])

    # Si todavía hay elementos en la lista2
    if lista2:
        permutar_recursivo(lista1, lista2[1:], permutaciones, actual + [lista2[0]])

def permutar_listas(lista1, lista2):
    permutaciones = []
    permutar_recursivo(lista1, lista2, permutaciones)
    return permutaciones

# Ejemplo de uso
lista1 = [5, 6]
lista2 = [1, 2,3,4]
resultado = permutar_listas(lista1, lista2)


for p in resultado:
    print(p)


end_time = time.perf_counter()
print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
