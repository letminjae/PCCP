# 2583 - 영역 구하기

import sys
input = sys.stdin.readline
from collections import deque

# 좌표를 꺾어서 0,0이 왼쪽위로 오게 만드는게 편하다.
M, N, K = map(int, input().split()) # M이 가로, N가 세로, K가 직사각형 갯수

graph = [[0]*M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

answer = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    queue = deque([])
    queue.append((x,y))
    graph[x][y] = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 0:
                    graph[next_x][next_y] = 1
                    queue.append((next_x, next_y))
                    cnt += 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt = 1
            bfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))

for i in answer:
    print(i, end=" ")