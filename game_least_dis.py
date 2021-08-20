def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    maps = padding(maps, n, m)
    position = [1, 1]
    stack = []
    while position != [n, m]:
        if maps[position[0]+1][position[1]]:
            position[0] += 1
        elif maps[position[0]][position[1]+1]:
            position[1] += 1
        elif maps[position[0]-1][position[1]]:
            position[0] -= 1
        elif maps[position[0]][position[1]-1]:
            position[1] -= 1
        else:
            break
    return answer


def padding(arr, n, m):
    temp = [[0] * (len(arr[0]) + 2) for _ in range(len(arr) + 2)]
    for i in range(1, n + 1):
        for j in range(1, m+1):
            temp[i][j] = arr[i-1][j-1]
    return temp

print(padding([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],5,5))