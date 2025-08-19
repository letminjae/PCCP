# 14940 - 쉬운 최단거리

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split()) # 세로 가로
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

def bfs():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2: # 시작점
                queue.append((i,j))
                visited[i][j] = 0
            elif graph[i][j] == 0: # 갈수없는 벽
                visited[i][j] = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cur_col, cur_row = queue.popleft()

        for i in range(4):
            next_y = cur_col + dy[i]
            next_x = cur_row + dx[i]

            if 0 <= next_y < N and 0 <= next_x < M:
                if visited[next_y][next_x] == -1 and graph[next_y][next_x] == 1:
                    visited[next_y][next_x] = visited[cur_col][cur_row] + 1
                    queue.append((next_y, next_x))

bfs()

for row in visited:
    print(*row)