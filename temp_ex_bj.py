import sys
input = sys.stdin.readline

from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def solution(seat):
    answer = 0
    l = len(seat)
    for i in range(l):
        seat[i] = list(seat[i])

    for i in range(l):
        for j in range(l):
            if seat[i][j] == 'C':
                step = 0
                q = deque([(i, j, step)])
                seat[i][j] = '-'
                while q:
                    x, y, st = q.popleft()
                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]
                        if new_x < 0 or new_y < 0 or new_x >= l or new_y >= l:
                            continue
                        if st == 2 and seat[new_x][new_y] == 'N':
                            answer += 1
                            seat[new_x][new_y] = '-'
                            continue
                        if seat[new_x][new_y] == 'N' or seat[new_x][new_y] == 'M':
                            answer += 1
                            seat[new_x][new_y] = '-'
                        q.append((new_x, new_y, st + 1))

    return answer

print(solution(["M--NN-", "-M----", "-CC--M", "-N----", "N-M-C-", "-M----"]))
