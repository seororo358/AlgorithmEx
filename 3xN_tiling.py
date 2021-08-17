def solution(n):
    answer = 0
    if n % 2:
        return 0
    dp = [0] * (n // 2 + 1)

    dp[0] = 1
    dp[1] = 3

    for i in range(2, n // 2 + 1):
        dp[i] = (4 * dp[i - 1] - dp[i - 2]) % 1000000007

    answer = dp[n // 2]
    return answer