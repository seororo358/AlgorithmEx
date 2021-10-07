import math


def solution(n):
    n -= 1
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return i

    return n