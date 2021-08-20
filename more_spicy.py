import heapq as hq ##heapq 라이브러리

def solution(scoville, K):
    answer = 0
    q = [] ## heap을 담을 리스트
    for i in scoville:
        hq.heappush(q, i) # scoville 배열에 있는 요소들을 heap으로 만듦

    while q[0] <= K: # K보다 최소힙이 크면 빠져나옴
        first = hq.heappop(q)
        if not q: # q가 빌때 까지 K값에 도달하지 못하면 answer을 -1로 놓고 반복문 탈출
            answer = -1
            break
        second = hq.heappop(q) # 두번째로 작은 값
        hq.heappush(q, first + 2 * second) # 합쳐진 음식의 스코빌지수를 힙에 삽입
        answer += 1
    return answer