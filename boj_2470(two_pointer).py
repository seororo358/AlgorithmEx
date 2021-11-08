import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n-1
Min = 1e10
answer = [0, n-1]
while left < right:
    temp = abs(arr[left] + arr[right])
    if temp < Min:
        Min = temp
        answer[0] = arr[left]
        answer[1] = arr[right]
        if temp == 0:
            break
    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -= 1
print(str(answer[0]) + " " + str(answer[1]))
