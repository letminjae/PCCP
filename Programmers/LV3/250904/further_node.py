# 프로그래머스 LV3 - 가장 먼 노드

# BFS로 풀어서 1번 노드에서 가장 멀리 떨어져 있는 거리를 구하기

from collections import deque

# BFS로 거리 탐색하여 방문거리를 1씩 늘린다.

def bfs(graph, visited):
    queue = deque([1]) # 노드 1부터 시작한다.
    visited[1] = 0 # 노드 1의 거리는 0이다.

    while queue:
        current_node = queue.popleft()

        for node in graph[current_node]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = visited[current_node]+1

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)

    # 노드에 간선을 연결한다.
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    bfs(graph, visited)
    
    max_distance = max(visited)

    for distance in visited:
        if distance == max_distance:
            answer += 1
    
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])