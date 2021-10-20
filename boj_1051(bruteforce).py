import sys

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline())[:m])
answer = 1
for k in range(min(n, m)-1, 0, -1):
    for i in range(len(arr)):
        if i + k >= n:
            break
        for j in range(len(arr[0])):
            if j + k >= m:
                break
            if arr[i][j] == arr[i+k][j+k] and arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i][j+k]:
                answer = k + 1
                break
        if answer:
            break
    if answer:
        break
print(answer**2)
