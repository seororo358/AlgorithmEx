import sys

r, c, q = map(int, sys.stdin.readline().split())
arr = []
queries = []
for _ in range(r):
    arr.append(list(map(int, sys.stdin.readline().split())))
for _ in range(q):
    queries.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(r):
    for j in range(c):
        if i > 0:
            arr[i][j] += arr[i-1][j]
        if j > 0:
            arr[i][j] += arr[i][j-1]
        if i > 0 and j > 0:
            arr[i][j] -= arr[i-1][j-1]
for r1, c1, r2, c2 in queries:
    temp = arr[r2-1][c2-1]
    if r1 > 1:
        temp -= arr[r1-2][c2-1]
    if c1 > 1:
        temp -= arr[r2-1][c1-2]
    if c1 > 1 and r1 > 1:
        temp += arr[r1-2][c1-2]
    print(temp//((r2-r1+1)*(c2-c1+1)))
