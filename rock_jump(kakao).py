def solution(stones, k):
    answer = 0
    max_c = 200000001
    min_c = 1
    while max_c >= min_c:
        mid = (max_c + min_c) // 2
        count = 0
        is_true = True
        for i in stones:
            if i - mid <= 0:
                count += 1
                if count == k:
                    is_true = False
                    break
            else:
                count = 0
        if is_true:
            min_c = mid + 1
            answer = min_c
        else:
            max_c = mid - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
