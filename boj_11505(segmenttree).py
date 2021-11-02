import sys
input = sys.stdin.readline
inf = 1000000007


def _init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (_init(start, mid, node*2) * _init(mid+1, end, node*2 + 1)) % inf
    return tree[node]


def _update(start, end, node, idx):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (_update(start, mid, node*2, idx) * _update(mid+1, end, node*2+1, idx)) % inf
    return tree[node]


def prod(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (prod(start, mid, node*2, left, right) * prod(mid+1, end, node*2+1, left, right)) % inf


n, m, k = map(int, input().split())
tree = [0] * (n * 4)
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
_init(0, n-1, 1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
        _update(0, n-1, 1, b-1)
    elif a == 2:
        print(prod(0, n-1, 1, b-1, c-1))
    else:
        pass
