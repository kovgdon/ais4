
def dfs(edges, start):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    visited = set()
    stack = [start]
    path = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return path

# Пример использования:
edges = [(4, 2), (1, 3), (2, 4)]
print(dfs(edges, 1))  # Вывод: [1, 3]