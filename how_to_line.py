from math import factorial


def solution(n, k):
    arr = [i for i in range(1, n+1)]
    answer = []
    fac = [0] * (n-1)

    if k == factorial(n):
        arr.reverse()
        return arr

    for i in range(1, n):
        fac[i-1] = factorial(i)

    while k > 1:
        for i in range(len(fac)-1, 0, -1):
            if k == fac[i]:
                answer.append(arr.pop(0))
                arr.reverse()
                k -= fac[i]
                break
            elif k > fac[i]:
                answer.append(arr.pop(k // fac[i]))
                k = k % fac[i]
                del fac[i:]
                break
            elif k < fac[i]:
                answer.append(arr.pop(0))
            else:
                pass
    answer += arr

    return answer


print(solution(8, 4))
