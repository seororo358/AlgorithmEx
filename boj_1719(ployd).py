import sys
input = sys.stdin.readline
inf = int(1e9)
n, m = map(int, input().split())
distance = [[inf]*(n+1) for _ in range(n+1)]
board = [['-'] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0
for _ in range(m):
    row, col, dis = map(int, input().split())
    distance[row][col] = dis
    distance[col][row] = dis
    board[row][col] = col
    board[col][row] = row
for k in range(1, n+1):
    for i in range(1, n+1):
        if k == i:
            continue
        for j in range(1, n+1):
            if k == j:
                continue
            if distance[i][k] + distance[k][j] < distance[i][j]:
                board[i][j] = board[i][k]
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j], end=' ')
    print()
