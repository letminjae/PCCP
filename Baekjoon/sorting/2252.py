# 2252 - 줄 세우기 (골드 3)
# 위상 정렬

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# 진입 차수
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    # B가 후순위이니 B 대기순서를 올린다
    indegree[B] += 1

def topology_sort():
    result = []
    q = deque()

    # 1. 진입 차수가 없는(0인) 학생을 순서대로 큐에 먼저 넣기
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 2. 큐가 빌 때까지 반복해서 정렬
    while q:
        now_node = q.popleft()
        result.append(now_node)

        for next_node in graph[now_node]:
            indegree[next_node] -= 1
            # 새롭게 진입차수가 0이 된 학생을 큐에 넣기
            if indegree[next_node] == 0:
                q.append(next_node)

    print(*result)

topology_sort()