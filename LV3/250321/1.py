# 이중우선순위 큐

from heapq import heappop, heappush, heapify

def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        command, num = op.split()
        num = int(num)
        if command == 'I': # I 일때
            heappush(min_heap, num)
            heappush(max_heap, (-num, num)) # 최대힙 구현을 위한 튜플구조 사용
        elif command == 'D': # D일 때
            if not min_heap:
              continue
            if num == 1: # 최댓값 삭제
              max_value = heappop(max_heap)[1]
              min_heap.remove(max_value)
              heapify(min_heap)
            else: # 최솟값 삭제
              min_value = heappop(min_heap)
              max_heap.remove((-min_value, min_value))
              heapify(max_heap)

    if not min_heap:
        return [0, 0]
    else:
        return [max(min_heap), min(min_heap)]
  
solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]) # [0,0]