import sys

input = sys.stdin.readline


def lazy_propagation(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def init_tree(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, node * 2) + init_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


def update(start, end, node, left, right, num):
    lazy_propagation(node, start, end)
    if left > end or right < start:
        return tree[node]
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * num
        if start != end:
            lazy[node * 2] += num
            lazy[node * 2 + 1] += num
        return tree[node]
    mid = (start + end) // 2
    tree[node] = update(start, mid, node * 2, left, right, num) + update(mid + 1, end, node * 2 + 1, left, right, num)
    return tree[node]


def sum_tree(start, end, node, left, right):
    lazy_propagation(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum_tree(start, mid, node * 2, left, right) + sum_tree(mid + 1, end, node * 2 + 1, left, right)


n, m, k = map(int, input().split())
arr = [0] * n
tree = [0] * (4 * n)
lazy = [0] * (4 * n)
for i in range(n):
    arr[i] = int(input())
init_tree(0, n - 1, 1)
for _ in range(m + k):
    qry = list(map(int, input().split()))
    if qry[0] == 1:
        update(0, n - 1, 1, qry[1] - 1, qry[2] - 1, qry[3])
    else:
        print(sum_tree(0, n - 1, 1, qry[1] - 1, qry[2] - 1))
