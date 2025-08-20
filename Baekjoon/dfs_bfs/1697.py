# 1697 - 숨바꼭질
# 가장 빠른 시간 = 최소 횟수 => BFS로 풀자

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001

def bfs(N):
    queue = deque([N])
    visited[N] = 0

    while queue:
        X = queue.popleft()

        dx_list = [X-1, X+1, X*2]

        if X == K:
            return visited[K]

        for dx in dx_list:
            if 0 <= dx <= 100000 and visited[dx] == -1:
                visited[dx] = visited[X] + 1
                queue.append(dx)
    return -1

print(bfs(N))