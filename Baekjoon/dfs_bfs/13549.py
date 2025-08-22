# 13549 - 숨바꼭질 3
# 2*X는 0초로 카운팅된다.
# 0초는 현재레벨에서 바로 처리되어야한다.

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

        back = X-1
        front = X+1
        jump = X*2

        if X == K:
            return visited[K]

        # 0초이동이 제일 먼저와야하므로 appendleft 사용
        if 0 <= jump <= 100000 and visited[jump] == -1:
            visited[jump] = visited[X]
            queue.appendleft(jump)

        if 0 <= back <= 100000 and visited[back] == -1:
            visited[back] = visited[X]+1
            queue.append(back)

        if 0 <= front <= 100000 and visited[front] == -1:
            visited[front] = visited[X]+1
            queue.append(front)

    return -1

print(bfs(N))