# 게임 맵 최단거리 - BFS 생각하며

from collections import deque
def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4): # 0, 1, 2, 3
                nx = x + dx[i]
                ny = y + dy[i]
                print("nx, ny : ", nx, ny)

                # 맵을 벗어나면 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                  continue

                # 벽이면 무시
                if maps[nx][ny] == 0:
                  continue

                # 노드가 1이라면, 좌표에 1 추가
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
 
    return -1 if answer == 1 else answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])