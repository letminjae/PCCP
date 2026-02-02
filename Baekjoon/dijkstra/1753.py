# 1753 - 최단경로 (골드 4)
# 다익스트라 (Dijkstra)

import sys
input = sys.stdin.readline
import heapq

# 입력, 그래프 초기화
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

# distance 배열 INF로 초기화
distance = [float("inf")] * (V+1)

# 다익스트라 함수 정의
def dijkstra(start):
    q = []
    # (거리, 노드) 순으로 heappush
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 거리 짧은 노드 정보 pop
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for v, w in graph[node]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])