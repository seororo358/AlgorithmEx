def find_child(graph, child, visited, a):
    visited[a] = True
    for i in graph[a]:
        if visited[i]:
            continue
        child[a] += find_child(graph, child, visited, i)

    return child[a]


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    child = [1] * (n + 1)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    child[1] = find_child(graph, child, visited, 1)

    for i in range(1, n + 1):
        child[i] = abs(n - 2 * child[i])
    answer = min(child[1:])

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
