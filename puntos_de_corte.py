from collections import defaultdict

# Clase para representar el grafo
class Grafo:
    def __init__(self, V):
        self.V = V
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def encontrar_puntos_corte(self):
        # Inicialización de variables
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        articulaciones = set()
        tiempo = [0]  # Variable mutable para rastrear el tiempo

        # DFS para encontrar puntos de corte
        def dfs(u):
            hijos = 0
            disc[u] = low[u] = tiempo[0]
            tiempo[0] += 1

            for v in self.grafo[u]:
                if disc[v] == -1:  # Si `v` no ha sido visitado
                    hijos += 1
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])

                    # Condiciones para punto de corte
                    if parent[u] == -1 and hijos > 1:  # Caso raíz
                        articulaciones.add(u)
                    if parent[u] != -1 and low[v] >= disc[u]:  # Caso general
                        articulaciones.add(u)

                elif v != parent[u]:  # Si `v` ya fue visitado y no es el padre
                    low[u] = min(low[u], disc[v])

        # Llamar a DFS para cada nodo no visitado
        for i in range(self.V):
            if disc[i] == -1:
                dfs(i)

        return sorted(articulaciones)

# Leer entrada
entrada = input().split()
V, E = map(int, entrada[:2])
grafo = Grafo(V)

for _ in range(E):
    u, v = map(int, input().split())
    grafo.agregar_arista(u - 1, v - 1)

# Encontrar y mostrar los puntos de corte en el grafo
puntos_corte = grafo.encontrar_puntos_corte()
print(" ".join(map(lambda x: str(x + 1), puntos_corte)))
