# 등굣길

def solution(m, n, puddles):
    map = [[0]*m for _ in range(n)]
    map[0][0] = 1

    # 웅덩이는 -1로 표시
    for x, y in puddles:
        map[y-1][x-1] = -1

    for i in range(n):
        for j in range(m):
            if map[i][j] == -1:
                map[i][j] = 0
                continue
            if i > 0:
                map[i][j] += map[i-1][j]
            if j > 0:
                map[i][j] += map[i][j-1]

    return map[n-1][m-1] % 1000000007