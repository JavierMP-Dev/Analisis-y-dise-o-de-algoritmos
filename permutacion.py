"""
Dado un array de tamaño N, genere e imprima todas las permutaciones posibles de los elementos R en array. Por ejemplo, si la matriz de entrada es {1, 2, 3, 4} y R es 2 (P(4,2)=12), entonces la salida debe ser:
{1, 2}, {2, 1}, {1, 3}, {3, 1}, {1, 4}, {4, 1}, {2, 3}, {3, 2}, {2, 4}, {4, 2}, {3, 4}, {4, 3}
"""
import time
start_time = time.perf_counter()

r = {4,2}
n = {1,2,3,4}

def ordenar_arreglos(n,r):
    # Ordena los arreglos de menor a mayor
    return sorted(r,n)


def generar_permutaciones(n, r):
    # Si el número de elementos a elegir es igual al número total de elementos, solo hay    
    # una permutación posible, que es la misma que el conjunto original
    for elementos in n:
        print("(" + str(elementos)+",")
        for eleme in r:
            print("," + str(eleme)+")")
"""
for elementos in n:
    print(elementos)

for eleme in r:
    print(eleme)
"""
generar_permutaciones(n,r)

end_time = time.perf_counter()
print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")