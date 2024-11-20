"""
Dado un laberinto en forma de matriz rectangular, encuentre un camino desde
una fuente dada hasta un destino dado. El camino solo se puede construir a 
partir de celdas que representen un muro y sin salirse de los límites; 
en cualquier momento, solo podemos movernos un paso en una de las cuatro direcciones: Arriba, Derecha, Abajo e Izquierda, es decir, usando una topología de cuatro vecinos y en sentido contrario a las agujas del reloj.
intentando hacer el programa del laberinto
"""

from collections import deque

# Función para ejecutar el BFS y resolver el problema
def resolver_laberinto(R, C, Sr, Sc, Tr, Tc, O, laberinto):
    # Movimientos en las 4 direcciones: Arriba, Derecha, Abajo, Izquierda
    direcciones = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]
    
    # Cola para BFS que contiene tuplas (fila, columna, longitud, camino)
    cola = deque([(Sr, Sc, 0, "")])
    visitado = set([(Sr, Sc)])
    
    # BFS para encontrar el camino
    while cola:
        x, y, longitud, camino = cola.popleft()
        
        # Si alcanzamos el destino, procesamos según el valor de O
        if (x, y) == (Tr, Tc):
            if O == 1:
                print("True")
            elif O == 2:
                print(longitud)
            elif O == 3:
                print(camino)
            return

        # Explorar los vecinos
        for dx, dy, direccion in direcciones:
            nx, ny = x + dx, y + dy
            
            # Verificar que el movimiento es válido
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visitado and laberinto[nx][ny] == ' ':
                visitado.add((nx, ny))
                cola.append((nx, ny, longitud + 1, camino + direccion))

    # Si no encontramos el camino
    if O == 1:
        print("False")
    elif O == 2 or O == 3:
        print(-1)

# Ejemplo de entrada
R, C, Sr, Sc, Tr, Tc, O = 10, 10, 1, 1, 8, 8, 1
laberinto = [
    "##########",
    "#     #  #",
    "# #   #  #",
    "# ### #  #",
    "#   # #  #",
    "#   #   ##",
    "# ###    #",
    "# #   #  #",
    "#     #  #",
    "##########"
]

# Convertimos el laberinto en una lista de listas
laberinto_matriz = [list(fila) for fila in laberinto]

# Llamada a la función con los datos de entrada
resolver_laberinto(R, C, Sr, Sc, Tr, Tc, O, laberinto_matriz)
