# 10828 스택

import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    order = input()
    
    # push X
    if 'push' in order:
        push, X = order.split()
        stack.append(int(X))
        
    # pop
    if 'pop' in order:
        if stack:
            pop = stack.pop()
            print(pop)
        else:
            print(-1)
    
    # size
    if 'size' in order:
        print(len(stack))
        
    # empty
    if 'empty' in order:
        if stack:
            print(0)
        else:
            print(1)
    
    # top
    if 'top' in order:
        if stack:
            print(stack[-1])
        else:
            print(-1)