from math import factorial

def solution(n, k):
    arr = [i for i in range(1,n+1)]
    answer = []
    fac = [0] * (n-1)

    for i in range(1,n):
        fac[i-1] = factorial(i)

    while k > 1:
        num = 0
        for i in range(len(fac)-1,0,-1):
            if k == fac[i]:
                arr.reverse()
                answer += arr
                del arr[:]
                k -= fac[i]
                break

            elif k > fac[i]:
                num = k // fac[i]
                k = k % fac[i]
                del fac[i:]
                answer.append(arr.pop(num))
                break

            else:
                answer.append(arr.pop(0))
    answer += arr

    return answer

print(solution(7,300))