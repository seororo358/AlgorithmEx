import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v+1)]
arr = []
for _ in range(e):
    v1, v2, cost = map(int, input().split())
    arr.append((cost, v1, v2))
arr.sort(reverse=True)
answer = 0
while arr:
    c, a, b = arr.pop()
    if find_parent(a) == find_parent(b):
        continue
    union_find(a, b)
    answer += c
print(answer)
