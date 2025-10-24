# 1654 랜선 자르기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = list(int(input()) for _ in range(K))
start, end = 1, max(lan)

while start <= end:
    mid = (start+end) // 2
    sum = 0

    for l in lan:
        sum += l // mid

    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)