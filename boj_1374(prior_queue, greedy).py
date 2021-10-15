import heapq as hq
import sys

N = int(input())
lec = []
q = []
for _ in range(N):
    n, start, end = map(int, sys.stdin.readline().split())
    lec.append((start, end))
lec.sort(reverse=True)
hq.heappush(q, lec.pop()[1])
Max = 1
while lec:
    if not q:
        hq.heappush(q, lec.pop()[1])
        continue
    if lec[-1][0] < q[0]:
        hq.heappush(q, lec.pop()[1])
        if len(q) > Max:
            Max = len(q)
    else:
        hq.heappop(q)

answer = Max

print(answer)
