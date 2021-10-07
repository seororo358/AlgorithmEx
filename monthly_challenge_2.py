def solution(n, left, right):
    answer = []
    start = (left // n, left % n)
    last = (right // n, right % n)

    if start[0] == last[0]:
        for i in range(left // n, left // n + 1):
            for j in range(left % n, right % n + 1):
                answer.append(max(i, j) + 1)
    else:
        for i in range(left // n, left // n + 1):
            for j in range(left % n, n):
                answer.append(max(i, j) + 1)
        for i in range(left // n + 1, right // n):
            for j in range(0, n):
                answer.append(max(i, j) + 1)
        for i in range(right // n, right // n + 1):
            for j in range(0, right % n + 1):
                answer.append(max(i, j) + 1)

    return answer