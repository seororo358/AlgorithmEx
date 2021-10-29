import sys

def find_par(x):
    if parent[x] == x:
        return x
    parent[x] = find_par(parent[x])
    return parent[x]

def union(a,b):
    a = find_par(a)
    b = find_par(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

while m > 0:
    query = list(map(int, sys.stdin.readline().split()))
    if query[0]:
        if find_par(query[1]) == find_par(query[2]):
            print("YES")
        else:
            print("NO")
    else:
        union(query[1], query[2])
    m -= 1
