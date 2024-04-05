from collections import deque, defaultdict

graph = defaultdict(list)

V, E = map(int, input().split())
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# def is_biprtite(graph):
#     visited, red, blue = set(), set(), set()
#     red.add(list(graph.keys())[0])

#     for node in graph:
#         if _is_biprtite(graph, node, visited, red, blue) and not blue.intersection(red):
#             return "bipartite"
#     return "not bipartite"


# def _is_biprtite(graph, node, visited, red, blue):
#     if node in red and node in blue:
#         return False

#     visited.add(node)

#     for neighbor in graph[node]:
#         if node in red:
#             blue.add(neighbor)
#         elif node in blue:
#             red.add(neighbor)

#         if neighbor not in visited:
#             _is_biprtite(graph, neighbor, visited, red, blue)

#     return True


def is_biprtite(graph):

    for node in graph:
        if _is_biprtite(graph, node):
            return "bipartite"
    return "not bipartite"


def _is_biprtite(graph, node):
    red = {node}
    blue = set()
    visited = set()
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node in blue and node in red:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if node in red:
                    blue.add(neighbor)
                elif node in blue:
                    red.add(neighbor)

                if node in red and neighbor in red or node in blue and neighbor in blue:
                    return False

                queue.append(neighbor)

    return True


print(is_biprtite(graph))
