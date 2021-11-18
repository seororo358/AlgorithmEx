import sys
input = sys.stdin.readline

n = int(input())
arr = []
answer = 0
for _ in range(n):
    arr.append(int(input()))
arr.sort()
num = arr[:]
for i in range(n):
    arr[i] += n-i
large = max(arr)
for i in range(n):
    if num[i]+n < large:
        continue
    answer += 1

print(answer)
