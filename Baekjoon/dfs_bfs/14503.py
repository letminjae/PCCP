# DFS는 아니지만 비스무리한 구현문제
# 14503 - 로봇 청소기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
start_row, start_col, start_direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cleaned_count = 0
r, c, d = start_row, start_col, start_direction

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    # 청소해야 되면 2로 graph 값을 바꾼다
    if graph[r][c] == 0:
        graph[r][c] = 2
        cleaned_count += 1

    found_flag = False

    # 네 방향 탐색
    for _ in range(4):
        # 반시계 방향 90도 회전
        d = (d+3) % 4
        nx = dx[d] + r
        ny = dy[d] + c

        # 바라보는 칸이 청소되지 않았으면 전진하고 break
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            r, c = nx, ny
            found_flag = True
            break
    
    # 네 방향 모두 벽 또는 청소가 되어있음 (못 가는 경우)
    if not found_flag:
        # 바라보는 방향의 뒤쪽 칸 계산
        back_x = r - dx[d]
        back_y = c - dy[d]

        # 뒤쪽이 벽이 아니면 후진한다
        if 0 <= back_x < N and 0 <= back_y < M and graph[back_x][back_y] != 1:
            r, c = back_x, back_y
        else:
            # 후진 못하면 break
            break

print(cleaned_count)