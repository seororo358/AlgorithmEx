from collections import deque as dq

v, e, start = map(int, input().split())
visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
dfs = []
bfs = []

for i in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for node in graph:
    node.sort(reverse=True)

st = [start]
while st:
    t = st.pop()
    if visited[t]:
        continue
    visited[t] = True
    dfs.append(t)
    st.extend(graph[t])
q = dq([start])
visited = [False] * (v + 1)
while q:
    t = q.popleft()
    if visited[t]:
        continue
    visited[t] = True
    bfs.append(t)
    q.extend(reversed(graph[t]))

for i in dfs:
    print(i, end= ' ')
print()
for i in bfs:
    print(i, end= ' ')