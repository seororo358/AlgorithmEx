import sys

n, k = map(int, sys.stdin.readline().split())
arr = [True] * (n+1)
start = 2
answer = 0
while start <= n:
    if not arr[start]:
        start += 1
        continue
    for i in range(start, n+1):
        if i % start or not arr[i]:
            continue
        else:
            k -= 1
            arr[i] = False
            if k == 0:
                answer = i
                break
    if answer > 0:
        break
print(answer)
