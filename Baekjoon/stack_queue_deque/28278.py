# 28278 스택 2

import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        stack.append(int(order[1]))

    elif order[0] == '2':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)

    elif order[0] == '3':
        print(len(stack))

    elif order[0] == '4':
        if stack:
            print(0)
        else:
            print(1)

    else:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)