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


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    if find_parent(v1) == find_parent(v2):
        continue
    union_find(v1, v2)
for i in range(1, n+1):
    parent[i] = find_parent(i)
par_set = set(parent[1:])
print(len(par_set))
