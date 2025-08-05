# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (N+1)
parents = [0] * (N+1)

def dfs(node):
    visited[node] = True
    for neighnor in arr[node]:
        if not visited[neighnor]:
            parents[neighnor] = node
            dfs(neighnor)

dfs(1)

for i in range(2, len(parents)):
    print(parents[i])