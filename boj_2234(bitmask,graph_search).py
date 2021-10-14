import sys
from collections import deque as dq

wall = [1, 2, 4, 8]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
n, m = map(int, sys.stdin.readline().split())
arr = []
maxi = 0
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
graph = [[0] * n for _ in range(m)]
num = 1
sector = dict()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = num
            q = dq([(i, j)])
            num1 = 0
            while q:
                nx, ny = q.popleft()
                num1 += 1
                for k in range(4):
                    if arr[nx][ny] & wall[k]:
                        continue
                    if graph[nx+dx[k]][ny+dy[k]] == 0:
                        graph[nx + dx[k]][ny + dy[k]] = num
                        q.append((nx+dx[k], ny+dy[k]))
            sector[num] = num1
            num += 1
            if num1 > maxi:
                maxi = num1
answer = []
for i in range(m):
    for j in range(n):
        for x, y in (1,0),(0,1):
            if x+i >= m or y+j >= n:
                continue
            if graph[i][j] != graph[i+x][j+y]:
                answer.append(sector[graph[i][j]] + sector[graph[i+x][j+y]])
print(num - 1)
print(maxi)
print(max(answer))
