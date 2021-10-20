import sys
sys.setrecursionlimit(1e9)


def dfs(x, w):
    for i in graph[x]:
        t, c = i
        if d[t] == -1:
            d[t] = w + c
            dfs(t, w + c)


n = int(input())
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

d = [-1] * (n+1)
d[1] = 0
dfs(1, 0)
start = d.index(max(d))
d = [-1] * (n+1)
d[start] = 0
dfs(start, 0)
print(max(d))
