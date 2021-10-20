import sys


def bin_search(s, e, arr, num):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return 0


T = int(input())
while T > 0:
    N = int(input())
    arr_n = list(map(int, sys.stdin.readline().split()))
    arr_n.sort()
    M = int(input())
    arr_m = list(map(int, sys.stdin.readline().split()))

    for i in arr_m:
        print(bin_search(0, N-1, arr_n, i))
    T -= 1
