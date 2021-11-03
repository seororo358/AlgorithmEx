import sys
from collections import deque as dq
input = sys.stdin.readline
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input())[:m])

for i in range(n):
    for j in range(m):
        board[i][j] = int(board[i][j])

answer = 0
q = dq([(0, 0, 1)])
board[0][0] = 0
while q:
    x, y, step = q.popleft()
    if x == n-1 and y == m-1:
        answer = step
        break
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_y < 0 or new_x < 0 or new_x >= n or new_y >= m:
            continue
        if board[new_x][new_y]:
            q.append((new_x, new_y, step+1))
            board[new_x][new_y] = 0

print(answer)
