import math


def solution(n, words):
    word_set = set()
    q = []
    num = 0
    for word in words:
        num += 1
        if not word_set:
            word_set.add(word)
            q.append((word[0], word[-1]))
            continue
        if word in word_set:
            break
        else:
            if q[-1][-1] == word[0]:
                q.append((word[0], word[-1]))
                word_set.add(word)
            else:
                break

    if len(word_set) == len(words):
        answer = [0, 0]
    else:
        if num % n:
            answer = [num % n, math.ceil(num / n)]
        else:
            answer = [n, math.ceil(num / n)]

    return answer