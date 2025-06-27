# 9375 패션왕 신해빈

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    wears = {}

    for _ in range(n):
        name, type = input().split()
        if type in wears:
            wears[type].append(name)
        else:
            wears[type] = [name]

    cnt = 1

    for x in wears:
        cnt *= (len(wears[x]) + 1)
    
    print(cnt-1)