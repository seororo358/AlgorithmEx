import sys
from collections import deque as dq
input = sys.stdin.readline

t = int(input())
while t > 0:
    t -= 1
    query = input()[:-1]
    n = int(input())
    arr = input()[1:-2]
    if query.count('D') > n:
        print("error")
        continue
    if arr:
        arr = list(map(int, arr.split(',')))
    arr = dq(arr)
    b_rev = False

    for i in query:
        if i == 'R':
            b_rev = not b_rev
        else:
            if b_rev:
                arr.pop()
            else:
                arr.popleft()
    if b_rev:
        arr.reverse()
    arr = list(arr)
    arr = str(arr)
    print(''.join(arr.split()))
