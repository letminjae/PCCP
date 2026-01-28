# 1406 - 에디터

import sys
input = sys.stdin.readline

stack_1 = list(input().strip())
stack_2 = []
N = int(input())

for i in range(N):
    C = input().split()
    if C[0] == 'L' and stack_1:
        stack_2.append(stack_1.pop())
    elif C[0] == 'D' and stack_2:
        stack_1.append(stack_2.pop())
    elif C[0] == 'B' and stack_1:
        stack_1.pop()
    elif C[0] == 'P':
        stack_1.append(C[1])

stack_1.extend(reversed(stack_2))
print(''.join(stack_1))