# 1182 부분수열의 합

import sys
input = sys.stdin.readline
from itertools import combinations

N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = 0

for i in range(1, N+1):
    combi = list(combinations(arr, i))

    for c in combi:
        if sum(c) == S:
            answer += 1

print(answer)