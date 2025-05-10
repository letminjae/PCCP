# 택배상자

from collections import deque

def solution(order):
    answer = 0
    belt = deque([])
    i = 0

    for box in range(1, len(order)+1):
        belt.append(box)

        while belt and belt[-1] == order[i]:
            answer += 1
            i += 1
            belt.pop()

    return answer