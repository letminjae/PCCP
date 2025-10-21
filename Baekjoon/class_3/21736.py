# 21736 헌내기는 친구가 필요해

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    
    while q:
        current_y, current_x = q.popleft()
    
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if 0<= ny < N and 0<= nx < M and not visited[ny][nx]:
                if graph[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    if graph[ny][nx] == 'P':
                        cnt += 1
start = (0, 0)
for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            start = (i, j)

bfs(start[0], start[1])

if cnt == 0:
    print("TT")
else:
    print(cnt)