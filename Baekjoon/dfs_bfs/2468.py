# 2468 - 안전영역(실버 1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 문제의 제한사항에 따라 재귀 깊이 늘림

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_rain = 0
answer = 1

for i in range(N):
    for j in range(N):
        if max_rain < graph[i][j]:
            max_rain = graph[i][j]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(y, x, num):
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x

        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx] and graph[ny][nx] > num:
                visited[ny][nx] = True
                dfs(ny, nx, num)

for rain in range(max_rain):
    visited = [[False]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > rain and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j, rain)
    
    answer = max(answer, cnt)

print(answer)