from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
q = deque()
res = [0] * (n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append((i, 1))
while q:
    now, cnt = q.popleft()
    res[now] = cnt
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i, cnt+1))
for i in res[1:n]:
    print(i, end=" ")
print(res[-1])
