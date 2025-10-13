# 11286 절댓값 힙
# ABS Heap 알고리즘

import sys, heapq
input = sys.stdin.readline

N = int(input())
abs_heap = []

for i in range(N):
    number = int(input())

    if number:
        heapq.heappush(abs_heap, (abs(number),number))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)