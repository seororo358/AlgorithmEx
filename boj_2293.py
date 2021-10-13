import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
dp = [0] * (K+1)
dp[0] = 1
for i in coin:
    for j in range(i, K+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[K])
