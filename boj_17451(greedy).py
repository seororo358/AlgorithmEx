import sys

answer = 0
n = int(input())
v = list(map(int, sys.stdin.readline().split()))
while v:
    num = v.pop()
    if num >= answer:
        answer = num
    else:
        if answer % num:
            answer = num * (answer // num + 1)

print(answer)
