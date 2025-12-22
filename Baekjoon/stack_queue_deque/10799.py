# 10799 - 쇠막대기

import sys
input = sys.stdin.readline

arr = list(input().strip())
stack = []
answer = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    else:
        # 레이저
        if arr[i-1] == '(':
            stack.pop()
            answer += len(stack)
        # 막대기
        else:
            stack.pop()
            answer += 1

print(answer)