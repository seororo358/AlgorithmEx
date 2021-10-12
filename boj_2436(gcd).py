import sys
import math


def gcd(a, b):
    if b % a:
        return gcd(b % a, a)
    else:
        return a


N, M = map(int, sys.stdin.readline().split())
temp = M // N
answer = [0, 0]
for i in range(int(math.sqrt(temp)), 0, -1):
    if temp % i:
        continue
    else:
        if gcd(i, temp//i) == 1:
            answer[0] = N * i
            answer[1] = N * (temp//i)
            break

print(answer[0], answer[1])
