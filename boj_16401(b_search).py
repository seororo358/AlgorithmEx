import sys

m, n = map(int, sys.stdin.readline().split())
cookie = list(map(int, sys.stdin.readline().split()))
mini = 1
maxi = max(cookie)
answer = 0
while mini <= maxi:
    pivot = (mini+maxi)//2
    ans = 0
    for i in cookie:
        ans += i // pivot
    if ans >= m:
        answer = pivot
        mini = pivot + 1
    else:
        maxi = pivot - 1
print(answer)
