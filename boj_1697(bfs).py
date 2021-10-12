import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001
q = deque([(N, 0)])
visited[N] = True
answer = 0
while q:
    pos, step = q.popleft()
    if pos == K:
        answer = step
        break
    if pos+1 <= 100000 and not visited[pos+1]:
        q.append((pos+1, step + 1))
        visited[pos+1] = True
    if not visited[pos-1] and pos-1 > -1:
        q.append((pos-1, step + 1))
        visited[pos-1] = True
    if pos*2 <= 100000 and not visited[pos*2]:
        q.append((pos*2, step + 1))
        visited[pos*2] = True

print(answer)