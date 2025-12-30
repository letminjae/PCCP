# 15655 - N과 M 6

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [False] * N
temp = []

def backtracking(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):
        if not visited[i]:
            temp.append(arr[i])
            visited[i] = True
            backtracking(i+1)
            temp.pop()
            visited[i] = False

backtracking(0)