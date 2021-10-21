import sys
from collections import deque as dq
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
m, n = map(int, sys.stdin.readline().split())
tomato = []
q = dq()
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j, 0))
num = 0
while q:
    nx, ny, count = q.popleft()
    if count > num:
        num = count
    for i in range(4):
        new_x = nx + dx[i]
        new_y = ny + dy[i]
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
        if tomato[new_x][new_y] == 0:
            tomato[new_x][new_y] = 1
            q.append((new_x, new_y, count+1))

full = True
for i in range(n):
    for j in range(m):
        if not tomato[i][j]:
            full = False
            break
    if not full:
        break
if full:
    print(num)
else:
    print(-1)
