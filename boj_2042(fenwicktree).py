import sys
input = sys.stdin.readline

def update(idx, dif):
    while idx <= n:
        tree[idx] += dif
        idx += (idx & -idx)


def sum(idx):
    answer = 0
    while idx > 0:
        answer += tree[idx]
        idx -= (idx & -idx)
    return answer


n, m, k = map(int, input().split())
tree = [0] * (n + 1)
arr = [0] * (n + 1)
for i in range(1, n+1):
    arr[i] = int(input())
    update(i, arr[i])

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
    elif a == 2:
        print(sum(c) - sum(b-1))
    else:
        pass
