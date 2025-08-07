# 2667 단지 번호 찾기

import sys
input = sys.stdin.readline

N = int(input())
graph = [[int(char) for char in input().strip()] for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [0, 0, -1, 1] # 상하우좌
dy = [-1, 1, 0, 0] # 상하우좌

def dfs(col, row):
    visited[col][row] = True
    # 이미 단지 1개를 세므로 초기값은 1이다.
    count = 1

    # 1. 네 방향을 모두 반복문을 돈다.
    for i in range(4):
        next_col = col + dy[i]
        next_row = row + dx[i]
    
        # 2. 위치에 따른 유효한 조건
        # 2-1. 맵의 범위를 벗어나지 않는지?
        if 0 <= next_col < N and 0 <= next_row < N:
            # 2-2. 조건을 만족하는지? => 이동한 곳에 집이 있고, 방문하지 않았으면 dfs 돌기
            if graph[next_col][next_row] == 1 and not visited[next_col][next_row]:
                count += dfs(next_col, next_row)
    
    return count

sizes = []

for col in range(N):
    for row in range(N):
        # 그래프가 1이고 (집이 있고), 방문하지 않은 곳이라면 조건 충족
        if graph[col][row] == 1 and not visited[col][row]:
            sizes.append(dfs(col, row))

print(len(sizes))

sizes.sort()

for size in sizes:
    print(size)