import heapq as hq

def solution(info, edges):
    answer = 0
    graph = [[] for i in range(len(info))]
    #늑대수,뎁스
    table = [0] * len(info)
    visited = [False] * len(info)

    for edge in edges:
        graph[edge[0]].append((edge[1],info[edge[1]]))

    def dfs(graph, i, visited, wolf, num):
        visited[i] = True
        if not graph[i]:
            return
        table[i] = (wolf, num)
        for k,j in graph[i]:
            if not visited[k]:
                if j:
                    dfs(graph, k, visited, wolf+1, num + 1)
                else:
                    dfs(graph, k, visited, wolf, num + 1)

    dfs(graph, 0, visited, 0, 0)
    table.sort(key = lambda x: x[1])
    depth = 0
    for i in range(len(table)):
        if depth == table[i][1]:
            if
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))