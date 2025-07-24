# 1260 DFS와 BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph =[[] for _ in range(N+1)]

for _ in range(M): # 양방향 간선 구하기
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

# DFS
def dfs(node):
    visited_dfs[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

# BFS
def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True
    print(start_node, end=' ')
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)
                print(neighbor, end=' ')

dfs(V)
print()
bfs(V)
print()