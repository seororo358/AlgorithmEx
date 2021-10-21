n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.reverse()

before_i = arr[0]
answer = 0
for i in arr[1:]:
    if i >= before_i:
        answer += i - before_i + 1
        before_i -= 1
    else:
        before_i = i
print(answer)
