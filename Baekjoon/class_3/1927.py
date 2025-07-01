# 1927 최소 힙

import sys
input = sys.stdin.readline
N = int(input())

import heapq

heap = []

for _ in range(N):
    number = int(input())

    if number == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, number)