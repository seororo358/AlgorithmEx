from collections import deque as dq


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(land, height):
    answer = 0
    n, m = len(land), len(land[0])
    sector = [[0] * m for _ in range(n)]
    num = 1
    graph = dict()

    for i in range(n):
        for j in range(m):
            if not sector[i][j]:
                queue = dq([(i, j)])
                sector[i][j] = num
                while queue:
                    c_x, c_y = queue.popleft()
                    for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                        new_x, new_y = x + c_x, y + c_y
                        if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                            continue
                        if not sector[new_x][new_y] and abs(land[c_x][c_y] - land[new_x][new_y]) <= height:
                            sector[new_x][new_y] = num
                            queue.append((new_x, new_y))
                num += 1

    for i in range(n):
        for j in range(m):
            for x, y in (1, 0), (0, 1):
                t_x, t_y = x + i, y + j
                if t_x < 0 or t_y < 0 or t_x >= n or t_y >= m:
                    continue
                if sector[t_x][t_y] == sector[i][j]:
                    continue
                elif sector[t_x][t_y] < sector[i][j]:
                    if (sector[t_x][t_y], sector[i][j]) not in graph.keys():
                        graph[(sector[t_x][t_y], sector[i][j])] = [abs(land[i][j] - land[t_x][t_y])]
                    else:
                        graph[(sector[t_x][t_y], sector[i][j])].append(abs(land[i][j] - land[t_x][t_y]))
                else:
                    if (sector[i][j], sector[t_x][t_y]) not in graph.keys():
                        graph[(sector[i][j], sector[t_x][t_y])] = [abs(land[i][j] - land[t_x][t_y])]
                    else:
                        graph[(sector[i][j], sector[t_x][t_y])].append(abs(land[i][j] - land[t_x][t_y]))
    edges = []
    parent = [i for i in range(num)]

    for s in graph.keys():
        edges.append((min(graph[s]), s[0], s[1]))
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer


print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],
               1))
