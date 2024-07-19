# 더 맵게

# 힙으로 풀기
import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        cnt += 1
    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))