# 1197 - 최소 스패닝 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())

parents = [i for i in range(V+1)] # 0 1 2 3

roads = [list(map(int, input().split())) for _ in range(E)]
roads.sort(key=lambda x:x[2])

def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_elements(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

answer = 0

for u,v,c in roads:
    if find_parents(parents, u) != find_parents(parents,v):
        answer += c
        union_elements(parents, u, v)

print(answer)