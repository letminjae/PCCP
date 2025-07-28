# 1012 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 문제의 제한사항에 따라 재귀 깊이 늘림

TC = int(input())

# 이동 배열
dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

def dfs(y, x):
    # 1. 현재 칸 방문 처리
    visited[y][x] = True

    # 2. 상하좌우의 이웃 칸 탐색
    for i in range(4): # 상, 하, 좌, 우
        next_y, next_x = y + dy[i], x + dx[i]

        # 3. 밭의 범위를 벗어나지 않는지 확인
        if 0 <= next_y < N and 0 <= next_x < M:
            # 4. 배추가 있는 칸이면서 + 방문 하지 않은 칸인지 확인
            if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
                # 재귀 호출
                dfs(next_y, next_x) 

# TC 별로 수행
for _ in range(TC):
    # 가로, 세로, 배추
    M, N, K = map(int, input().split())

    # 초기화 그리드
    grid = [[0]*M for _ in range(N)]

    # 이미 방문한 배추를 다시 세지않게 설정
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    # 지렁이 개수
    answer = 0             
    
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 1 and not visited[row][col]:
                answer += 1
                dfs(row, col)

    print(answer)