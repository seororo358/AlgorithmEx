def solution(money):
    dp = [[0] * len(money) for _ in range(2)]
    maximum = [0, 0]

    dp[0][0] = money[0]
    dp[0][1] = money[1]
    dp[0][2] = money[2] + money[0]

    for i in range(3, len(money) - 1):
        if dp[0][i - 2] < dp[0][i - 3]:
            dp[0][i] = dp[0][i - 3] + money[i]
        else:
            dp[0][i] = dp[0][i - 2] + money[i]

    maximum[0] = max(dp[0])
    money.reverse()

    dp[1][0] = money[0]
    dp[1][1] = money[1]
    dp[1][2] = money[2] + money[0]

    for i in range(3, len(money) - 1):
        if dp[1][i - 2] < dp[1][i - 3]:
            dp[1][i] = dp[1][i - 3] + money[i]
        else:
            dp[1][i] = dp[1][i - 2] + money[i]

    maximum[1] = max(dp[1])
    answer = max(maximum)

    return answer