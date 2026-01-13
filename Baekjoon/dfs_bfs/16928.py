# 16928 - 뱀과 사다리 게임

import sys
input = sys.stdin.readline
from collections import deque

# graph 만들기
graph = [[0]*10 for _ in range(10)]
num = 1
for i in range(10):
    for j in range(10):
        graph[i][j] = num
        num += 1

# 사다리와 뱀 좌표
ladders_and_snakes = {}
l, s = map(int, input().split())
for _ in range(l+s):
    x, y = map(int, input().split())
    ladders_and_snakes[x] = y

# BFS 수행
def bfs(start_node):
    # 큐 만들어서 시작 노드 입력
    q = deque([start_node])

    # visited로 주사위 횟수 기록
    visited = [-1]*101 # 인덱스 보정
    visited[start_node] = 0

    while q:
        current = q.popleft()

        # 종료조건 : current가 100이면 종료
        if current == 100:
            return visited[current]

        # 주사위를 굴려서 이동되는 수 모두 찾기
        for i in range(1, 7):
            next_node = current + i

            if next_node <= 100:
                # next_node에 뱀과 사다리가 있으면 next_node 갱신
                if next_node in ladders_and_snakes:
                    next_node = ladders_and_snakes[next_node]

                # visited 갱신
                if visited[next_node] == -1:
                    visited[next_node] = visited[current]+1
                    q.append(next_node)

print(bfs(1))