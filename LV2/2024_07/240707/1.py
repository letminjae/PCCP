# 프로세스

from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)
    while dq:
        mx = max(dq)
        left = dq.popleft()

        location -= 1

        if left != mx:
            dq.append(left)
            if location < 0:
                location = len(dq) - 1
        else:
            answer += 1
            if location < 0:
                break
            
    return answer

print(solution([1, 1, 9, 1, 1, 1],0))