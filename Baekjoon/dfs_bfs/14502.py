# 14502 - 연구소
# 0은 빈 칸, 1은 벽, 2는 바이러스
# 3개의 벽을 어떻게 세워야하는지에 대한 경우의 수 계산

import sys
input = sys.stdin.readline
import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split()) #세로, 가로
graph = [list(map(int, input().split())) for _ in range(N)]

empty_area = [] # 빈 영역의 좌표를 넣는 리스트
virus_area = [] # 바이러스의 좌표를 넣는 리스트
safety_area = 0 # 안전영역 - 정답

# 1. 빈칸(0)과 바이러스(2)의 좌표를 확인한다
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_area.append((i, j))
        elif graph[i][j] == 2:
            virus_area.append((i, j))

# 2. 3개의 벽을 넣은 조합 만들기
wall_combinations = combinations(empty_area, 3)

# 3. BFS 만들기
def bfs(wall_graph):
    queue = deque(virus_area)
    visited = [[False]*M for _ in range(N)] # 매번 초기화 필요
    for col, row in virus_area:
        visited[col][row] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cur_col, cur_row = queue.popleft()

        for i in range(4):
            next_y = cur_col + dy[i]
            next_x = cur_row + dx[i]

            if 0 <= next_y < N and 0 <= next_x < M:
                if visited[next_y][next_x] == False and wall_graph[next_y][next_x] == 0:
                    visited[next_y][next_x] = True
                    wall_graph[next_y][next_x] = 2
                    queue.append((next_y, next_x))

# 4. 벽을 넣은 그래프에서 bfs 수행
# 좌표 읽으면서 반복문 수행
for combo in wall_combinations:
    # 조합마다 원본 그래프 깊은복사 필요
    wall_graph = copy.deepcopy(graph)
    current_safty_area = 0

    # 벽을 3개 넣는다
    for y, x in combo:
        wall_graph[y][x] = 1

    # 벽을 다 넣고 bfs 수행
    bfs(wall_graph)

    # bfs를 모두 수행한 wall_graph 결과의 0 갯수를 읽는다
    for i in range(N):
        for j in range(M):
            if wall_graph[i][j] == 0:
                current_safty_area += 1
    
    safety_area = max(safety_area, current_safty_area)

print(safety_area)