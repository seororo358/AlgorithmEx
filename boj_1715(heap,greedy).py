import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
q = []
answer = 0
for i in range(n):
    hq.heappush(q, int(input()))

while len(q) > 1:
    a = hq.heappop(q)
    b = hq.heappop(q)
    answer += a + b
    hq.heappush(q, a + b)
print(answer)
