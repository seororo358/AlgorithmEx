import sys
input = sys.stdin.readline
def update(idx, dif):
    while(idx <= n):
        tree[idx] += dif
        idx += (idx & -idx)


n, m, k = map(int, input().split())
tree = [0] * n
for i in range(n):
    tree[i] = int(input())
for _ in range(m+k):
    a, b, c = map(int, input().split())
