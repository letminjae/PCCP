# 16724 - 피리 부는 사나이 (골드 3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
answer = 0

dist = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1)
}

visited = [[0]*M for _ in range(N)]

def dfs(y, x):
    global answer
    visited[y][x] = 1

    direction = graph[y][x]
    dy, dx = dist[direction]
    ny, nx = y + dy, x + dx

    if visited[ny][nx] == 0:
        dfs(ny, nx)
    elif visited[ny][nx] == 1:
        answer += 1
    
    # 탐색이 끝났으면 현재 노드는 2로 변경
    visited[y][x] = 2

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)

print(answer)