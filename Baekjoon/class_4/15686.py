# 15686 치킨게임

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 집
            houses.append((i,j))
        elif graph[i][j] == 2: # 치킨집
            chickens.append((i,j))

def cal_chicken(hx, hy, bx, by):
    return abs(hx-bx) + abs(hy-by)

chickens_idx = [i for i in range(len(chickens))]
min_number = 9999
combi = list(combinations(chickens_idx, M))

while combi:
    total = 0
    atom = combi.pop()

    for i in range(len(houses)):
        min_distance = 9999
        
        for j in atom:
            x, y = chickens[j]
            min_distance = min(min_distance, cal_chicken(x, y, houses[i][0], houses[i][1]))
        
        total += min_distance
    
    min_number = min(min_number, total)

print(min_number)