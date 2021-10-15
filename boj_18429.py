from itertools import permutations as per
import sys

N, K = map(int, sys.stdin.readline().split())
kit = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    kit[i] -= K
answer = 0
for arr in per(kit, N):
    temp = 0
    answer += 1
    for i in arr:
        temp += i
        if temp < 0:
            answer -= 1
            break
print(answer)
