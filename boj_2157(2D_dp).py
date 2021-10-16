from collections import deque as dq
import sys

n, m, k = map(int, input().split())
Map = [[0] * 301 for _ in range(301)]
for _ in range(k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a > b:
        continue
    Map[a][b] = max(c, Map[a][b])

dp = [[0] * 301 for _ in range(301)]
q = dq([(1, 1)])

while q:
    index, cnt = q.popleft()
    if cnt >= m:
        break
    if index == n:
        continue
    for i in range(1, n+1):
        if Map[index][i]:
            q.append((i, cnt+1))
    for i in range(index+1, n+1):
        dp[cnt][i] = max(dp[cnt][i], dp[cnt-1][index] + Map[index][i])
answer = list()
for i in range(1, m):
    answer.append(dp[i][n])

print(max(answer))
