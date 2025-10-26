''' 17/10/2025 '''

# import heapq

# graph = {
#     "A":{"B":5, "C":2},
#     "B":{"A":5, "D":1},
#     "C":{"A":2, "D":8},
#     "D":{"B":1, "C":8}
# }

# def dijkstar(graph, start):

#     distances = {node: float("inf") for node in graph}
#     distances[start] = 0
#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distances, current_node = heapq.heappop(priority_queue)

#         if current_distances > distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node].items():
#             new_distances = current_distances + weight

#             if new_distances < distances[neighbor]:
#                 distances[neighbor] = new_distances
#                 heapq.heappush(priority_queue, (new_distances, neighbor))

#     return distances

# print(dijkstar(graph, "A"))






graph = {
    "A":{"B":5, "C":2},
    "B":{"A":5, "D":1},
    "C":{"A":2, "D":8},
    "D":{"B":1, "C":8}
}

def dijkstar(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):

        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node

        for neighbor, weght in graph[min_node].items():
            new_distance = distances[min_node] + weght
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        visited.add(min_node)
    return distances

print(dijkstar(graph, "A"))           

