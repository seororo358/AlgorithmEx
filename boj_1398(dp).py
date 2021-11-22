import sys
input = sys.stdin.readline
t = int(input())
coin = [1, 10, 25]
dp = [it for it in range(100)]
dp[0] = 0
for i in range(1, 3):
    for j in range(coin[i], 100):
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)
while t > 0:
    t -= 1
    money = int(input())
    ans = 0
    while money > 0:
        ans += dp[money % 100]
        money //= 100
    print(ans)
