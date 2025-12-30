# 15654 - N과 M 5

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

per = sorted(list(permutations(arr, M)))

for p in per:
    print(*p)