import sys
from bisect import bisect_right as bi_r
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
temp = arr[:]
arr.sort()
answer = 0
for idx, k in enumerate(temp):
    answer = max(answer, idx-bi_r(arr, k)+1)
answer += 1
print(answer)
