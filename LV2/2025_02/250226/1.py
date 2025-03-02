# 숫자 변환하기

# 최소 연산횟수 : BFS 사용

from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set([x])

    while queue:
        print(queue, visited)
        current, count = queue.popleft()

        if current == y:
            return count
        
        for num in (current + n, current * 2, current * 3):
            if num <= y and num not in visited:
                queue.append((num, count + 1))
                visited.add(num)

    return -1

solution(10, 40, 5) # 2