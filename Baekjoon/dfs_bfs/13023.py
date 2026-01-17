# 13023 - ABCDE (골드5)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
relation = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
    
visited = [False] * N
        
def dfs(v, depth):   
    if depth == 4:
        print(1)
        exit()
    
    for neighbor in relation[v]:
        if not visited[neighbor]:
            visited[v] = True
            dfs(neighbor, depth+1)
            visited[v] = False
            
for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    
print(0)