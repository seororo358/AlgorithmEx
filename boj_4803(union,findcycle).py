import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
T = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    for _ in range(m):
        c, d = map(int, input().split())
        if find_parent(c) != find_parent(d):
            union(c, d)
        else:
            union(c, 0)
            union(d, 0)
    for i in range(n+1):
        find_parent(i)
    set_par = set(parent)
    length = len(set_par) - 1
    if length == 0:
        print("Case " + str(T) + ": No trees.")
    elif length == 1:
        print("Case " + str(T) + ": There is one tree.")
    else:
        print("Case " + str(T) + ": A forest of " + str(length) + " trees.")
    T += 1
