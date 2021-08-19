from math import inf


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for edge in roads:
        if graph[edge[0]][edge[1]] > edge[2]:
            graph[edge[0]][edge[1]] = edge[2]
        else:
            pass

    return answer


##def find(start, graph, end, traps):


print(solution(25,[2, 14, 11, 21, 17],2))