import sys
mod = 1000000007


def power(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    if m % 2:
        return n * power(n, m-1)
    else:
        half = power(n, m//2)
        half %= mod
        return (half*half) % mod


N, K = map(int, sys.stdin.readline().split())

factorial = [1 for _ in range(N+1)]

for i in range(2, N+1):
    factorial[i] = factorial[i-1] * i % mod
A = factorial[N]
B = factorial[N-K] * factorial[K]

print((A % mod) * power(B, mod - 2) % mod)
