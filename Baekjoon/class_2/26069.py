# 26069 붙임성 좋은 총총이

import sys
input = sys.stdin.readline

N = int(input())

set_user = set()
set_user.add("ChongChong")

for _ in range(N):
    A, B = input().split()
    if A in set_user:
        set_user.add(B)
    elif B in set_user:
        set_user.add(A)

print(len(set_user))