import sys
N = int(sys.stdin.readline())

M = int(sys.stdin.readline())
answer = 0
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
first = 0
last = N-1
while first < last:
    if arr[first] + arr[last] == M:
        first += 1
        answer += 1
        last -= 1
    elif arr[first] + arr[last] < M:
        first += 1
    else:
        last -= 1
print(answer)
