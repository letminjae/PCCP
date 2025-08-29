# 15663 - N과 M 9

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

set_per = sorted(list(set(permutations(arr,M))))

for p in set_per:
    print(*p)