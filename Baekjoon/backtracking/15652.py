# 15652 - N과 M 4

import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

M, N = map(int, input().split())

arr = [int(i) for i in range(1, M+1)]

combi = list(combinations_with_replacement(arr,N))

for com in combi:
    print(*com)