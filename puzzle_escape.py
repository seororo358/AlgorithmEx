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

#트랩함수
def trap_on(graph, trap_num):
    for i in range(len(graph)):
        i += 1

    return


print(solution(3,1,3,[[1,2,2],[3,2,3]],[2]))
