# 15664 - N과 M 10

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [False] * N
temp = []
result = set()

def backtracking(start):
    if len(temp) == M:
        if not tuple(temp) in result:
            print(*temp)
            result.add(tuple(temp))
    
    for i in range(start, N):
        temp.append(arr[i])
        visited[i] = True
        backtracking(i+1)
        temp.pop()
        visited[i] = False

backtracking(0)