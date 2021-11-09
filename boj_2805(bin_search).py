import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
Min = 0
Max = max(tree)
answer = 0
while Min <= Max:
    mid = (Min + Max) // 2
    ans = 0
    for i in tree:
        if i <= mid:
            continue
        ans += i - mid
    if ans >= m:
        Min = mid + 1
        answer = mid
    else:
        Max = mid - 1
print(answer)
