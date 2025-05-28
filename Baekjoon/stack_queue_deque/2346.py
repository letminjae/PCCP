# 2346 풍선 터뜨리기

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

deq = deque(enumerate(map(int, input().split())))
answer = []

while deq:
    idx, now = deq.popleft()
    answer.append(idx + 1)

    if now > 0:
        deq.rotate(-(now - 1))
    elif now < 0:
        deq.rotate(-now)

print(' '.join(map(str, answer)))