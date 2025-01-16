# Author: Javier
# Date: 25/12/2024 
def buscador_conectados(V, E, edges):
    from collections import defaultdict, deque
    
    # Creando una lista de adyacencia
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (V + 1)
    components = []
    
    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return component
    
    
    #encontrando todos los componentes conectados
    
    for vertex in range(1, V + 1):
        if not visited[vertex]:
            component = bfs(vertex)
            components.append(sorted(component))
    
    return components

# leyendo las entradas del programa
V, E = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(E)]

# función para encontrar los componentes conectados
components = buscador_conectados(V, E, edges)

# imprimiendo los resultados
print(len(components))
for component in components:
    print(" ".join(map(str, component)))