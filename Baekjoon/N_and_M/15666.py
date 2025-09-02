# 15666 - N과 M 12

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
set_arr = sorted(list(set(arr)))

answer = []

def backtraking(start):
    global answer

    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(start, len(set_arr)):
        answer.append(set_arr[i])
        backtraking(i)
        answer.pop()

backtraking(0)