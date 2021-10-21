import sys
inf = 1e9
v, e = map(int, sys.stdin.readline().split())
graph = [[inf] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for i in range(1, v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Min = inf
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            continue
        Min = min(Min, graph[i][j] + graph[j][i])

if Min == inf:
    print(-1)
else:
    print(Min)
