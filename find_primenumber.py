from itertools import permutations as per
import math
arr = [True] * 10000000


def find_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrtn = int(math.sqrt(num))
    for div in range(3,sqrtn+1,2):
        if num % div == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    for k in range(1,len(numbers)+1):
        for i in per(numbers,k):
            num = int(''.join(i))
            if find_prime(num):
                answer += 1

    return answer

print(solution("17"))