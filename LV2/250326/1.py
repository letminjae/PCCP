# 삼각 달팽이

def solution(n):
    answer = [[0]*n for _ in range(n)]
    dir = [[1,0], [0,1], [-1,-1]] # 아래, 오른쪽, 왼쪽 대각선 방향
    dir_idx = 0
    num = n*n - sum([i+1 for i in range(n-1)]) # 달팽이 원소 총 갯수
    x = y = 0 # 좌표
    answer[x][y] = 1 # 초기값
    
    for i in range(2, num+1):
        dx, dy = dir[dir_idx % 3] # 다음 칸 이동
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or answer[nx][ny] != 0 :
            dir_idx += 1

            dx, dy = dir[dir_idx % 3] # 변경한 방향으로 이동
            nx = x + dx
            ny = y + dy
        
        x = nx
        y = ny
        answer[x][y] = i
    
    return [number for arr in answer for number in arr if number != 0]

solution(4)
# [1,2,9,3,10,8,4,5,6,7]