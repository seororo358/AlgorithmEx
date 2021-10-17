import sys
from collections import Counter

n, m, b = map(int, input().split())
Map = []
for _ in range(n):
    Map += list(map(int, sys.stdin.readline().split()))
_sum = sum(Map)
_len = n * m
land = Counter(Map)
Min = _sum // _len
ans_t, ans_g = 1e9, 0
for i in range(Min, 257):
    if i * _len > _sum + b:
        break
    time = 0
    for key in land:
        if key < i:
            time += (i - key) * land[key]
        else:
            time += (key - i) * land[key] * 2
    if time <= ans_t:
        ans_t = time
        ans_g = i

print(ans_t, ans_g)
