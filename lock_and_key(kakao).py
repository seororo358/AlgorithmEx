import copy
def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)
    rot = 0
    lock = padding(lock, n, m) ##자물쇠 주변 0추가

    while rot <= 3:
        for i in range(0, m + n - 1):## 하나씩 윈도윙
            for j in range(0, m + n - 1):
                lock_copy = copy.deepcopy(lock) ##자물쇠 복제본
                for k in range(0, n): ##키와 열쇠 요소 맞추기
                    for l in range(0, n):
                        lock_copy[i+k][j+l] = lock_copy[i+k][j+l] ^ key[k][l] ##lock과 key를 XOR
                answer = True
                for k in range(n - 1, n - 1 + m): ## 자물쇠의 모든 요소가 1로 초기화 되었는지 확인
                    for l in range(n - 1, n - 1 + m):
                        if lock_copy[k][l] == 0:
                            answer = False
                del lock_copy[:]
                if answer == True:
                    return True
        else: ## 윈도윙을 한 모든 경우에도 lock이 풀리지 않았을 경우 90도 회전
            key = rotate_90(key)
            rot += 1
    return answer


def rotate_90(arr): ## 키 회전 함수
    return list(zip(*arr[::-1]))

def padding(arr, n, m): ##자물쇠 주변 키 - 1만큼 패딩
    length = 2 * (n - 1) + m
    temp = [[0] * length for _ in range(length)]

    for i in range(n - 1, n - 1 + m):
        for j in range(n - 1, n - 1 + m):
            temp[i][j] = arr[i - n + 1][j - n + 1]

    return temp

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


