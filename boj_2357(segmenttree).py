import sys
input = sys.stdin.readline


def min_init(start, end, node):
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]
    mid = (start + end) // 2
    min_tree[node] = min(min_init(start, mid, node*2), min_init(mid+1, end, node*2+1))
    return min_tree[node]


def max_init(start, end, node):
    if start == end:
        max_tree[node] = arr[start]
        return max_tree[node]
    mid = (start + end) // 2
    max_tree[node] = max(max_init(start, mid, node*2), max_init(mid+1, end, node*2+1))
    return max_tree[node]


def min_find(start, end, node, left, right):
    if left > end or right < start:
        return 1e9
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start + end) // 2
    return min(min_find(start, mid, node*2, left, right), min_find(mid+1, end, node*2+1, left, right))


def max_find(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start + end) // 2
    return max(max_find(start, mid, node*2, left, right), max_find(mid+1, end, node*2+1, left, right))


n, m = map(int, input().split())
min_tree = [0] * (4*n)
max_tree = [0] * (4*n)
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
min_init(0, n-1, 1)
max_init(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(min_find(0, n-1, 1, a-1, b-1), max_find(0, n-1, 1, a-1, b-1))
