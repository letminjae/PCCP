# 3190 - 뱀

import sys
input = sys.stdin.readline
from collections import deque

# N*N 정사각형 보드 진행
N = int(input())
graph = [[0]*N for _ in range(N)]

# 보드에 사과를 저장
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2

# 뱀의 방향 변환 정보 = info로 저장
L = int(input())
info = {}
for _ in range(L):
    time, C = map(str, input().split())
    info[int(time)] = C

# 게임 초 (정답)
second = 0

# 시작 방향과 초기셋팅
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
current_dir = 1
x, y = 0, 0
graph[x][y] = 1
snake = deque([(0,0)])

# 방향 전환
def turn(direction, C):
    if C == 'D':
        return (direction + 1) % 4
    else:
        return (direction - 1) % 4

# 게임 시작
while True:
    second += 1

    # 1. 다음 위치 먼저 계산하기
    nx = x + dx[current_dir]
    ny = y + dy[current_dir]

    # 2.벽 또는 자기자신(1)과 부딪히면 게임 종료
    if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == 1:
        print(second)
        break

    # 3. 이동
    # 사과가 있는 경우
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        snake.appendleft((nx, ny))
    # 사과가 없는 경우
    else:
        graph[nx][ny] = 1
        snake.appendleft((nx, ny))
        tail_x, tail_y = snake.pop() # 꼬리 제거
        graph[tail_x][tail_y] = 0
    
    # 4. 좌표 업데이트
    x, y = nx, ny

    # 5. 방향 전환
    if second in info:
        current_dir = turn(current_dir, info[second])