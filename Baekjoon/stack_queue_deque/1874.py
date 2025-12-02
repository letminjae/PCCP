# 1874 - 스택 수열

import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

stack = [0]
current = 1
answer = []
is_possible = True

for number in arr:
    while current <= N and stack[-1] != number:
        stack.append(current)
        answer.append("+")
        current += 1
    
    if stack[-1] == number:
        stack.pop()
        answer.append("-")
    else:
        is_possible = False
        break

if is_possible:
    print('\n'.join(answer))
else:
    print("NO")