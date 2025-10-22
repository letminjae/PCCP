# 11403 경로 찾기

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(start):
    q = deque()
    q.append(start)
    connected = [0 for _ in range(N)]

    while q:
        x = q.popleft()

        for i in range(N):
            if connected[i] == 0 and graph[x][i] == 1:
                q.append(i)
                connected[i] = 1
                visited[start][i] = 1

for i in range(N):
    bfs(i)

for i in visited:
    print(*i)