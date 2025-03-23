# 야근지수 - 최대힙을 마이너스로 구현

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works)+1)
    return sum([work**2 for work in works])

solution(4, [4,3,3]) # 12