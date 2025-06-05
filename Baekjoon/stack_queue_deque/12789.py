# 12789 도키도키 간식드리미

import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
stack = []
flag = 1

for p in people:
    stack.append(p)

    while stack and stack[-1] == flag:
        stack.pop()
        flag += 1

if stack:
    print("Sad")
else:
    print("Nice")