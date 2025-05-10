# 전력망을 둘로 나누기

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]: 
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    min_diff = float('inf')

    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]

        # 그래프 구성
        graph = defaultdict(list)
        for x, y in temp_wires:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * (n+1) # 방문했는지 확인필요
        count = bfs(temp_wires[0][0], graph, visited)

        diff = abs((n-count) - count)
        min_diff = min(min_diff, diff)

    return min_diff