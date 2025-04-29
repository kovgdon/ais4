edges = [(4, 2), (1, 3), (2, 4)]

def dfs_path_length(edges, a, b):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    visited = set()
    stack = [(a, 0)]
    
    while stack:
        vertex, distance = stack.pop()
        if vertex == b:
            return distance
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                stack.append((neighbor, distance + 1))
    return -1  # Путь не найден

# # Пример использования:
# print(dfs_path_length(edges, 2, 4))  # Вывод: 1
# def dfs(edges, start):
#     graph = {}
#     for u, v in edges:
#         graph.setdefault(u, []).append(v)
#         graph.setdefault(v, []).append(u)
    
#     visited = set()
#     stack = [start]
#     path = []
    
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             path.append(vertex)
#             for neighbor in reversed(graph.get(vertex, [])):
#                 if neighbor not in visited:
#                     stack.append(neighbor)
#     return path

# # Пример использования:
# print(dfs(edges, 1))  # Вывод: [1, 3]