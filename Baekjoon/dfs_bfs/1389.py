# 1389 - 케빈 베이컨의 6단계 법칙

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    visited = [-1] * (N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        cur_node = queue.popleft()

        for next_node in arr[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + 1
                queue.append(next_node)

    cnt = sum(visited)
    return cnt

min_cnt = float("inf")
answer = 0

for i in range(1, N+1):
    total_cnt = bfs(i)

    if total_cnt < min_cnt:
        min_cnt = total_cnt
        answer = i

print(answer)