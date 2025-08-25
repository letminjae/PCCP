# 7562 - 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque

def bfs(M, start, end):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    
    queue = deque()
    queue.append(start)
    
    visited = [[-1] * M for _ in range(M)]
    visited[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == end[0] and y == end[1]:
            return visited[x][y]
        
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<= next_y < M and 0<= next_x < M and visited[next_x][next_y] == -1 :
                visited[next_x][next_y] = visited[x][y] + 1
                queue.append((next_x, next_y))

N = int(input().rstrip())

for _ in range(N):
    M = int(input().rstrip()) # 체스판의 길이
    currentX, currentY = map(int, input().rstrip().split()) # 현재 나이트의 위치
    destinationX, destinationY = map(int, input().rstrip().split()) # 내가 가고싶은 나이트의 위치
    
    start = (currentX, currentY)
    end = (destinationX, destinationY)
    
    print(bfs(M, start, end))