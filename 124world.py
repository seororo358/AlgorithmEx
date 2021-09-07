def solution(n):
    arr = []
    while n > 0:
        n -= 1
        arr.append(n % 3)
        n = n // 3

    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        elif arr[i] == 1:
            arr[i] = 2
        else:
            arr[i] = 4

    arr.reverse()
    arr = list(map(str, arr))
    answer = ''.join(arr)

    return answer
