import sys


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
for i in range(n):
    connected = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if connected[j]:
            union(i+1, j+1)
plan = list(map(int, sys.stdin.readline().split()))
root = find(plan[0])
isPossible = "YES"
for i in plan:
    if find(i) != root:
        isPossible = "NO"
        break
print(isPossible)
