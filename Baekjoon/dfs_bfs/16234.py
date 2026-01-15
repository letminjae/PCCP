# 16234 - 인구 이동 (골드 4) 
# Pypy3로 제출

import sys
input = sys.stdin.readline
from collections import deque

# 그래프 만들기
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(y, x, visited):
    q = deque([(y,x)])
    visited[y][x] = True

    # 연합과 인구수
    union = [(y,x)]
    total = graph[y][x]

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    while q:
        current_y, current_x = q.popleft()

        for i in range(4):
            ny = dy[i] + current_y
            nx = dx[i] + current_x

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                diff = abs(graph[current_y][current_x] - graph[ny][nx])
                # L, R 범위안에 들어왔을때 연합 추가
                if L <= diff <= R:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    union.append((ny,nx))
                    total += graph[ny][nx]
    
    if len(union) > 1:
        avg = total // len(union)
        for y, x in union:
            graph[y][x] = avg
        return True
    
    return False

days = 0

while True:
    visited = [[False]*N for _ in range(N)]
    is_moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    is_moved = True
    
    if not is_moved:
        break

    days += 1

print(days)