# 1520 - 내리막 길 (골드 3)
# DFS + DP

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

dp = [[-1]*M for _ in range(N)]

def dfs(y, x):
    if y == N-1 and x == M-1:
        return 1
    
    # 처음 오는 좌표면 0으로 계산 시작
    if dp[y][x] == -1:    
        dp[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < M and 0 <= ny < N and graph[y][x] > graph[ny][nx]:
                dp[y][x] += dfs(ny, nx)
    
    return dp[y][x]

print(dfs(0,0))