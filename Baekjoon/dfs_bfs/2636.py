# 2636 - 치즈

import sys
input = sys.stdin.readline
from collections import deque

# 그래프 만들기
N, M = map(int, input().split()) # 세로 가로
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 치즈가 녹는데 걸리는 시간
time = 0
last_cheese_count = 0

# 공기를 기준으로 bfs 작업
def bfs(y,x):
    q = deque([(y,x)])

    visited = [[False]*M for _ in range(N)]
    visited[y][x] = True

    melt_list = [] # 녹을 치즈 좌표 리스트

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    while q:
        current_y, current_x = q.popleft()

        # 상하좌우 반복해서 탐색
        for i in range(4):
            next_y = dy[i] + current_y
            next_x = dx[i] + current_x
 
            if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x]:
                visited[next_y][next_x] = True

                # 조건1 : 공기(0)을 만나면 큐에 넣고 탐색
                if graph[next_y][next_x] == 0:
                    q.append((next_y,next_x))
                # 조건2 : 치즈(1)을 만나면 melt_list에 좌표 저장
                elif graph[next_y][next_x] == 1:
                    melt_list.append((next_y, next_x))

    # melt_list에 있는 좌표를 0으로 모두 바꿈
    for cheese_y, cheese_x in melt_list:
        graph[cheese_y][cheese_x] = 0
    
    return len(melt_list)
                
while True:
    melted_count = bfs(0,0)

    # 종료 조건 : 이번에 녹은 치즈가 없음
    if melted_count == 0:
        break

    last_cheese_count = melted_count
    time += 1

print(time)
print(last_cheese_count)