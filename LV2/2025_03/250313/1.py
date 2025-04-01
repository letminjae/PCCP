# 쿼드압축 후 개수 세기

def quad(arr, r, c, size, answer):
    base = arr[r][c]

    for i in range(r, r+size):
        for j in range(c, c+size):
            if arr[i][j] != base:
                # 크기를 줄이고 재귀를 호출한다.
                size //= 2
                quad(arr, r, c, size, answer)
                quad(arr, r, c+size, size, answer)
                quad(arr, r+size, c, size, answer)
                quad(arr, r+size, c+size, size, answer)
                return # 이미 분할이 되었으면 return

    answer[base] += 1

def solution(arr):
    answer = [0,0]
    quad(arr, 0, 0, len(arr), answer)
    return answer


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) #[4, 9]