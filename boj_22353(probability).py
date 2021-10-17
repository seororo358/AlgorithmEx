a, d, k = map(int, input().split())
cur = d / 100
rate = 1 + k/100
arr = []
answer = 0
while cur < 1:
    arr.append(cur)
    cur *= rate
arr.append(1)

t = 0
for i in range(len(arr)):
    t += a
    r = 1
    for j in range(i):
        r *= (1-arr[j])
    r *= arr[i]
    answer += t * r

print(round(answer, 7))
