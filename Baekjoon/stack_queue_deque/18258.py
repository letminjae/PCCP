# 18258 큐 2

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

deq = deque([])

for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        deq.append(int(order[1]))
    elif order[0] == 'pop':
        if deq:
            left = deq.popleft()
            print(left)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    elif order[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)