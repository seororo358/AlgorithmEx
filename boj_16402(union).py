import sys
input = sys.stdin.readline


def find_parent(x):
    if kingdom[x] == x:
        return x
    kingdom[x] = find_parent(kingdom[x])
    return kingdom[x]


def union(par, child):
    par = find_parent(par)
    child = find_parent(child)
    kingdom[child] = par


n, m = map(int, input().split())
kingdom = dict()
for _ in range(n):
    temp = input()[11:-1]
    kingdom[temp] = temp
for _ in range(m):
    temp = list(input().split(','))
    if temp[-1][0] == '1':
        win = temp[0][11:]
        lose = temp[1][11:]
        if find_parent(win) != find_parent(lose):
            union(win, lose)
        else:
            kingdom[win] = win
            kingdom[lose] = win
    elif temp[-1][0] == '2':
        win = temp[1][11:]
        lose = temp[0][11:]
        if find_parent(win) != find_parent(lose):
            union(win, lose)
        else:
            kingdom[win] = win
            kingdom[lose] = win
for i in kingdom.keys():
    kingdom[i] = find_parent(i)
ans = list(set(kingdom.values()))
ans.sort()
print(len(ans))
for i in ans:
    print("Kingdom of " + i)
print(kingdom)
