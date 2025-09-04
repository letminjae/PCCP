# 1926 - 그림

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(y, x):
    visited[y][x] = True
    area = 1 # 현재 칸 넓이는 1

    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]

        if 0 <= next_y < N and 0 <= next_x < M:
            if not visited[next_y][next_x] and graph[next_y][next_x] == 1:
                area += dfs(next_y, next_x)
    
    return area

N, M = map(int, input().split()) # 세로 가로
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            current_area = dfs(i, j)
            max_area = max(max_area, current_area)

print(cnt)
print(max_area)