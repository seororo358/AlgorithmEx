
def solution(land, height):
    answer = 0
    sector = [[-1]*len(land[0]) for _ in range(len(land))]
    sector[0][0] = 0
    for i in range(len(land)):
        for j in range(len(land[0])):
            if sector[i][j] != -1:
                same_sector(land, sector, (i, j))
    return answer

def same_sector(land, sector, pos):

    return