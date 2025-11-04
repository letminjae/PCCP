# 7569 토마토
# 1: 익음, 0: 익지않음, -1: 없음

import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomatoes = []

def bfs():
    queue = deque()
    for tomato in tomatoes:
        queue.append(tomato)

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    dz = [-1, 1]

    while queue:
        z, x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[z][nx][ny] == 0:
                graph[z][nx][ny] = graph[z][x][y] + 1
                queue.append((z, nx, ny))
        # 상하
        for j in range(2):
            nz = z + dz[j]
            if 0 <= nz < H and graph[nz][x][y] == 0:
                graph[nz][x][y] = graph[z][x][y] + 1
                queue.append((nz, x, y))
                
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                tomatoes.append((z, x, y))

bfs()

answer = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            if graph[z][x][y] > answer:
                answer = graph[z][x][y]

print(answer-1)