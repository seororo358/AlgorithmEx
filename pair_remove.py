from collections import deque


def solution(s):
    answer = 0
    st = []
    arr = deque(s)
    if len(s) % 2:
        return 0
    while arr:
        if len(arr) == 1:
            if arr[0] == st[-1]:
                st.pop()
                arr.pop()
            else:
                pass
            break
        if arr[0] != arr[1]:
            if not st:
                st.append(arr.popleft())
                st.append(arr.popleft())
            else:
                if st[-1] == arr[0]:
                    st.pop()
                    arr.popleft()
                else:
                    st.append(arr.popleft())
        else:
            arr.popleft()
            arr.popleft()
    if not st:
        answer = 1

    return answer


print(solution('cdcd'))
