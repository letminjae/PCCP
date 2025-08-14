# 7576 - 토마토
# 토마토가 익는지에 대한 최소일수 - BFS로 풀자
# 중요한 점 : 익은토마토(1)가 있는 '모든' 칸이 BFS의 시작점이기에 BFS의 시작을 알리는 매개변수는 없다.

import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

def bfs():
    queue = deque()
    # 그래프를 순회하며 익은 토마토 찾기
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j)) # 익은 토마토 좌표를 찾아 queue에 넣어준다
                visited[i][j] = 0 # 익은 토마토 좌표 거리는 0으로 시작한다

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cur_col, cur_row = queue.popleft()

        for i in range(4):
            next_y = cur_col + dy[i]
            next_x = cur_row + dx[i]

            if 0 <= next_y < N and 0 <= next_x < M:
                if visited[next_y][next_x] == -1 and graph[next_y][next_x] == 0:
                    visited[next_y][next_x] = visited[cur_col][cur_row] + 1
                    queue.append((next_y, next_x))

bfs()
max_days = 0
# 거리 순회하며 max_days 갱신
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 and graph[i][j] == 0:
            print(-1) # 익지 않은 토마토가 있을 경우
            exit()
        if visited[i][j] > max_days:
            max_days = visited[i][j]
            
print(max_days)