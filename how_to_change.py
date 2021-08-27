def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    money.sort()

    for i in money:
        for j in range(1,n+1):
            if i <= j:
                dp[j] += dp[j-i]

    answer = dp[n]

    return answer

print(solution(5,[1,2,5]))