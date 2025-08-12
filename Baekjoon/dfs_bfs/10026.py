# 10026 - 적록색약
# 재귀 깊이가 깊어서 BFS로 푸는게 더 좋을 것 같다.

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[char for char in input().strip()] for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(start_col, start_row):
    queue = deque()
    queue.append((start_col, start_row))
    visited[start_col][start_row] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        col, row = queue.popleft()

        for i in range(4):
            next_y = col + dy[i]
            next_x = row + dx[i]

            # 범위를 넘어서지 않고 + 이전 노드와 색깔이 같고 + 방문을 안한 노드
            if 0 <= next_y < N and 0 <= next_x < N and graph[col][row] == graph[next_y][next_x] and visited[next_y][next_x] == 0:
                visited[next_y][next_x] = 1
                queue.append((next_y, next_x))


# 정상인 케이스 카운팅
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약 케이스 - G를 R로 변경
for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

# 적록색약 케이스 카운팅
visited = [[0]*N for _ in range(N)] # 방문여부 초기화
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)