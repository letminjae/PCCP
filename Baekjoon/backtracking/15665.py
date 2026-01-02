# 15665 - N과 M 11

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

temp = []
result = set()

def backtracking(start):
    if len(temp) == M:
        if tuple(temp) not in result:
            print(*temp)
            result.add(tuple(temp))
            return
        else:
            return

    for i in range(N):
        temp.append(arr[i])
        backtracking(i+1)
        temp.pop()

backtracking(0)