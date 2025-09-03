# 4963 - 섬의 개수
# 섬의 개수 - DFS, 가로-세로-대각선 모두 방문 필요

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def dfs(y, x):
    visited[y][x] = True

    for i in range(8):
        next_y = y + dy[i]
        next_x = x + dx[i]

        if 0 <= next_y < H and 0 <= next_x < W:
            if visited[next_y][next_x] == False and arr[next_y][next_x] == 1:
                dfs(next_y, next_x)

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = []
    for _ in range(H):
        row = list(map(int, input().split()))
        arr.append(row)

    cnt = 0
    visited = [[False] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if visited[i][j] == False and arr[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)