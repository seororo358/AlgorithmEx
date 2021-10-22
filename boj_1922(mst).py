import sys
import heapq as hq

inp = sys.stdin.readline
n = int(inp())
m = int(inp())
res = 0
q = []
parent = [i for i in range(n+1)]


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    s, e, cost = map(int, inp().split())
    hq.heappush(q, (cost, s, e))
edge = 0 # 최적화 : edge = vertex - 1
while q:
    cost, a, b = hq.heappop(q)
    if find(a) != find(b):
        union(a, b)
        res += cost
        edge += 1
    if edge == n - 1: # 최적화 : edge = vertex - 1
        break
print(res)
