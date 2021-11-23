import sys
import heapq as hq

input = sys.stdin.readline
n, k = map(int, input().split())
q = []
bags = []
for _ in range(n):
    hq.heappush(q, tuple(map(int, input().split())))
for _ in range(k):
    bags.append(int(input()))
bags.sort()
answer = 0
pack = []
for b in bags:
    while q and b >= q[0][0]:
        weight, value = hq.heappop(q)
        hq.heappush(pack, -value)
    if pack:
        answer -= hq.heappop(pack)

print(answer)
