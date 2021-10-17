import sys

tc = 1
arr = [[[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [0, 1], [1, 1], [1, 2]],
        [[0, 1], [1, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 1], [1, 1], [2, 1], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [0, 1], [1, 0], [2, 0]],
        [[0, 0], [1, 0], [2, 0], [1, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[1, 0], [0, 1], [2, 1], [1, 1]],
        [[1, 0], [0, 1], [1, 2], [1, 1]],
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        ]


def inside(nx, ny, n):
    return nx < 0 or ny < 0 or nx >= n or ny >= n


while True:
    n = int(input())
    if n == 0:
        break
    land = []
    for _ in range(n):
        land.append(list(map(int, sys.stdin.readline().split())) + [0, 0, 0, 0])
    for _ in range(4):
        land.append([0 for _ in range(n+4)])
    ans = -987654321
    for i in range(n):
        for j in range(n):
            for k in range(13):
                flag = 1
                _sum = 0
                for l in range(4):
                    nx = i + arr[k][l][0]
                    ny = j + arr[k][l][1]
                    if inside(nx, ny, n):
                        flag = 0
                        break
                    _sum += land[nx][ny]
                if flag:
                    ans = max(ans, _sum)
    print(str(tc) + ".", end=' ')
    print(ans)
    tc+=1
