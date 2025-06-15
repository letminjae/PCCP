# 정수 삼각형

def solution(triangle):
    for i in range(len(triangle)-2, -1, -1): # Bottom-Up
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) # 30