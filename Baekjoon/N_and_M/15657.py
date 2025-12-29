# 15657 - N과 M 8

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

temp = []

def backtracking(start):
    if len(temp) == M:
        print(*temp)
        return
    
    for i in range(start, N):
        temp.append(arr[i])
        backtracking(i)
        temp.pop()

backtracking(0)