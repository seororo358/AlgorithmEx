import sys
import bisect as bs
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr_sort = arr[:]
arr_sort.sort()
maxi = 0
for i in range(N):
    temp = bs.bisect_left(arr_sort, arr[i])
    if i-temp > maxi:
        maxi = i - temp
print(maxi)
