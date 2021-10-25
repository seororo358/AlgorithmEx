import sys
dy = [1, 1, 0, -1]
dx = [0, 1, 1, 1]

def omok(graph, num, pos, option, cnt):
    if cnt > 5:
        return False
    else:
        return omok(graph, num, [pos[0]+dx[option],pos[1]+dy[option]], option, cnt+1)

board = list()

for _ in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))
five = False
for i in range(19):
    for j in range(19):
        if board[i][j]:
            for k in range(4):
                if board[i][j] == board[i+dx[k]][j+dy[k]]:
                    five = omok(board, board[i][j], [i, j], k, 2)
