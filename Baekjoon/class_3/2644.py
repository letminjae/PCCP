# 2644 촌수 계산

# 최단거리 문제이므로, BFS로 문제 풀기
import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 총 인원
A, B = map(int, input().split()) # 촌수를 구해야하는 사람 2명
M = int(input()) # 부모 자식 간의 관계 수

graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1) # 촌 수의 거리

for _ in range(M):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(start_node, target_node):
    queue = deque([start_node])
    distance[start_node] = 0

    while queue:
        current_node = queue.popleft()

        if current_node == target_node:
            return distance[target_node]
        
        for neighbor in graph[current_node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current_node] + 1
                queue.append(neighbor)
        
    return -1

answer = bfs(A, B)
print(answer)