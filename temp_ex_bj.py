import heapq as hq
import sys
input = sys.stdin.readline

inf = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
dis = [inf] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []
hq.heappush(q,(0,start))
dis[start] = 0
while q:
    dist, now = hq.heappop(q)
    if dis[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            hq.heappush(q, (cost, i[0]))

for i in range(1, len(dis)):
    if dis[i] == inf:
        print("INF")
        continue
    print(dis[i])
