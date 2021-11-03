import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[1e9] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        if k == i:
            continue
        for j in range(n):
            if i == j or k == j:
                continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1e9:
            arr[i][j] = 0
        print(arr[i][j], end=' ')
    print()
