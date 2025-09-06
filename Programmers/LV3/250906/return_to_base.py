# 프로그래머스 LV3 - 부대복귀
# 전형적인 BFS 문제

'''
n = 총 지역의 수
roads = 왕복할 수 있는 길
sources = 부대원이 위치한 서로다른 지역들
destination = 강철부대의 지역
'''

from collections import deque

def bfs(n, graph, destination):
    queue = deque()
    visited = [-1] * (n+1)
    queue.append(destination)
    visited[destination] = 0
    
    while queue:
        current_node = queue.popleft()
        
        for next_node in graph[current_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[current_node] + 1
                queue.append(next_node)
    
    return visited

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    distance = bfs(n, graph, destination)
    
    for source in sources:
        answer.append(distance[source])
    
    return answer

solution(3,[[1, 2],[2, 3]],[2, 3],1)