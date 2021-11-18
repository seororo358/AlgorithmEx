import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
graph = [[] for _ in range(n)]
leaf = [1] * n
for i in range(n):
    if parent[i] == -1:
        continue
    graph[parent[i]].append(i)
idx = 0
for gr in graph:
    if gr:
        leaf[idx] = 0
    idx += 1
delete = int(input())
if parent[delete] == -1:
    print(0)
else:
    q = deque([delete])

    while q:
        num = q.popleft()
        if graph[num]:
            q.extend(graph[num])
        else:
            leaf[num] = 0
    if len(graph[parent[delete]]) == 1:
        leaf[parent[delete]] = 1
    print(sum(leaf))
