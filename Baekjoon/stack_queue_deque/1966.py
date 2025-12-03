# 1966 프린터 큐

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

for _ in range(N):
    n, number = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        max_number = max(queue)
        left = queue.popleft()
        number -= 1

        if max_number == left:
            cnt += 1
            if number < 0:
                print(cnt)
                break
        else:
            queue.append(left)
            if number < 0:
                number = len(queue)-1