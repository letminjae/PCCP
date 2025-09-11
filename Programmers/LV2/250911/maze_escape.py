# 프로그래머스 LV2 - 미로 탈출

from collections import deque

def bfs(start, end, maps):
    queue = deque()
    start_y, start_x = start
    queue.append((start_y, start_x))
    
    N, M = len(maps), len(maps[0])
    visited = [[-1]*M for _ in range(N)]
    visited[start_y][start_x] = 0
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    while queue:
        y, x = queue.popleft()
        
        if (y, x) == end:
            return visited[y][x]
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0<= next_y < N and 0<= next_x < M:
                if visited[next_y][next_x] == -1 and maps[next_y][next_x] != "X":
                    visited[next_y][next_x] = visited[y][x] + 1
                    queue.append((next_y, next_x))
                    
    return -1

def solution(maps):
    S, L, E = (), (), ()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                S = (i, j)
            elif maps[i][j] == "L":
                L = (i, j)
            elif maps[i][j] == "E":
                E = (i, j)
    
    dist1 = bfs(S, L, maps)
    dist2 = bfs(L, E, maps)
    
    if dist1 == -1 or dist2 == -1:
        return -1
    else:
        return dist1 + dist2

solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])