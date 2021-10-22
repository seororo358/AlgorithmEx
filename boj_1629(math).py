def power(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    if m % 2:
        return n * power(n, m-1)
    else:
        half = power(n, m//2)
        half %= c
        return (half*half) % c


a, b, c = map(int, input().split())

print(power(a, b) % c)
