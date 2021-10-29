import sys
from collections import deque as dq
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []
n, k = map(int, input().split())
board = []
time = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
q = dq([(x-1, y-1)])
while s >= 0:
    s -= 1
    st = []
    for item in q:
        cur_x, cur_y = item
        if board[cur_x][cur_y] > 0:
            answer.append(board[cur_x][cur_y])
            continue
        board[cur_x][cur_y] = -1
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if new_y < 0 or new_x < 0 or new_x >= n or new_y >= n:
                continue
            if board[new_x][new_y] == -1:
                continue
            st.append((new_x, new_y))

    if answer:
        break
    q.clear()
    q.extend(st)

if answer:
    print(min(answer))
else:
    print(0)
