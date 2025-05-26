# 28279 덱 2

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

deq = deque([])

for _ in range(N):
    order = input().split()
    if order[0] == '1':
        deq.appendleft(int(order[1]))
    elif order[0] == '2':
        deq.append(int(order[1]))
    elif order[0] == '3':
        if deq:
            left = deq.popleft()
            print(left)
        else:
            print(-1)
    elif order[0] == '4':
        if deq:
            left = deq.pop()
            print(left)
        else:
            print(-1)
    elif order[0] == '5':
        print(len(deq))
    elif order[0] == '6':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == '7':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else: # '8'
        if deq:
            print(deq[-1])
        else:
            print(-1)