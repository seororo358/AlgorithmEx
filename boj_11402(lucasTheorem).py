import sys

arr_n = []
arr_k = []
n, k, m = map(int, sys.stdin.readline().split())
fac = [1 for _ in range(m)]
for i in range(1, m):
    fac[i] = i * fac[i-1]
res = 1
while n > 0:
    arr_n.append(n % m)
    n //= m
while k > 0:
    arr_k.append(k % m)
    k //= m
for i in range(len(arr_k)):
    if arr_k[i] > arr_n[i]:
        res = 0
        break
    if arr_k[i] == 0 or arr_k[i] == arr_n[i]:
        continue
    res *= fac[arr_n[i]] // (fac[arr_k[i]] * fac[arr_n[i] - arr_k[i]])
    res %= m
print(res)
