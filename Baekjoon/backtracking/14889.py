# 14889 - 스타트와 링크

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 스타트팀인 경우
visited = [False] * N
min_diff = float('inf')

def backtracking(depth, index):
    global min_diff

    if depth == N//2:
        start_team = 0
        link_team = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_team += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += graph[i][j]

        min_diff = min(min_diff, abs(start_team-link_team))
        return
    
    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False
    
backtracking(0, 0)
print(min_diff)