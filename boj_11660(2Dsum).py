import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
arr.append([0]*(n+1))
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

for i in range(n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i][j-1]
for i in range(n+1):
    for j in range(1, n+1):
        arr[j][i] += arr[j-1][i]

query = []
for _ in range(m):
    query.append(list(map(int, input().split())))

for x1, y1, x2, y2 in query:
    answer = 0
    answer += arr[x2][y2] + arr[x1-1][y1-1] - arr[x2][y1-1] - arr[x1-1][y2]
    print(answer)
