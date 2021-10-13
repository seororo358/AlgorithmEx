import sys

T = int(sys.stdin.readline())
arr = [[] for _ in range(T)]
answer = []
for i in range(T):
    N = int(sys.stdin.readline())
    for _ in range(N):
        arr[i].append(tuple(map(int, sys.stdin.readline().split())))

for i in range(T):
    arr[i].sort()
    maxi = arr[i][0][1]
    ans = 0
    for k in arr[i]:
        if k[1] > maxi:
            continue
        else:
            maxi = k[1]
            ans += 1
    answer.append(ans)
for i in answer:
    print(i)
