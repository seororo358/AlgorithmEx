import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == m and y == n:
        return 1
    elif dp[x][y] == -1:
        dp[x][y] = 0
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 < new_x <= m and 0 < new_y <= n and arr[x][y] > arr[new_x][new_y]:
                dp[x][y] += dfs(new_x, new_y)
    return dp[x][y]


m, n = map(int, input().split())
dp = [[-1] * (n+1) for _ in range(m+1)]

arr = [[10001] * (n+1)]
for _ in range(m):
    arr.append([10001] + list(map(int, input().split())))
print(dfs(1, 1))
