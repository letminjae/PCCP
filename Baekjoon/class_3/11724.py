# 11724 연결 요소의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (N+1)
answer = 0

def dfs(node):
    visited[node] = True
    for neighbor in arr[node]:
        if not visited[neighbor]:
            dfs(neighbor)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)