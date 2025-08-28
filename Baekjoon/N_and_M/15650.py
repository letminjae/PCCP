# 15650 N과 M (2)

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

arr = list(num for num in range(1,N+1))
combi = list(combinations(arr, M))

for c in combi:
    print(*c)