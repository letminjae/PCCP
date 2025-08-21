# 12851 - 숨바꼭질 2
# 가장 빠른 시간 = 최소 횟수 => BFS로 풀자

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
count = [0] * 100001 # 해당 숫자에 도달하는 방법의 가짓수

def bfs(N):
    queue = deque([N])
    visited[N] = 0
    count[N] = 1

    while queue:
        X = queue.popleft()

        dx_list = [X-1, X+1, X*2]

        if X == K:
            return print(f'{visited[K]}\n{count[K]}')
            

        for dx in dx_list:
            if 0 <= dx <= 100000 and visited[dx] == -1:
                visited[dx] = visited[X] + 1
                count[dx] = count[X]
                queue.append(dx)
            # 이미 방문했지만, 최단시간으로 다시 도달한 경우
            elif 0 <= dx <= 100000 and visited[dx] == visited[X]+1:
                # visited는 최단 시간으로 채워져있으므로 건드리지 않는다. (무시)
                # 가짓수만 더한다
                count[dx] += count[X]
    return -1

bfs(N)