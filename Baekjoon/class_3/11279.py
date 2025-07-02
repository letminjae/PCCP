# 11279 최대 힙

import sys
input = sys.stdin.readline
N = int(input())

import heapq

max_heap = []

for _ in range(N):
    number = int(input())

    if number == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -number)