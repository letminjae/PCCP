# 2178 - 미로 찾기
# 최소칸의 수를 찾는 프로그램 - BFS 사용

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[int(char) for char in input().strip()] for _ in range(N)]
visited = [[-1] * M for _ in range(N)] # 거리문제는 False가 아닌 -1로 설정하는 것이 좋다.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1 # 시작점 거리는 1

    while queue:
        current_y, current_x = queue.popleft()

        # 현재 위치가 도착점이면 거리를 반환한다 (정답)
        if current_y == N-1 and current_x == M-1:
            return visited[current_y][current_x]

        # 상하좌우 탐색
        for i in range(4):
            next_y = current_y + dy[i]
            next_x = current_x + dx[i]

            # 범위를 벗어나지 않는지 + 노드가 1인지 + 이미 방문하지 않았는지
            if 0 <= next_y < N and 0 <= next_x < M and graph[next_y][next_x] == 1 and visited[next_y][next_x] == -1:
                # 다음 칸의 거리는 현재 칸의 거리 + 1
                visited[next_y][next_x] = visited[current_y][current_x] + 1
                queue.append((next_y, next_x)) # 다음 위치를 튜플로 큐에 다시 넣음
                
    return -1 # 도달하지 못한 경우

result = bfs(0,0)
print(result)