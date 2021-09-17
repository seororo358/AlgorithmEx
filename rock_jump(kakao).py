def solution(stones, k):
    answer = 0
    max_c = 200000001
    min_c = 1
    #rock 이분탐색 시작
    while max_c >= min_c:
        mid = (max_c + min_c) // 2
        count = 0
        is_true = True
        for i in stones:#이분탐색 시작시 통과사람수가 mid보다 많을경우
            if i - mid <= 0:
                count += 1
                if count == k:
                    is_true = False
                    break
            else:
                count = 0
        #이분탐색 결과 정리
        if is_true:
            min_c = mid + 1
            answer = min_c
        else:
            max_c = mid - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
