# 1987 - 알파벳
# DFS로 다시 풀이

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 시간초과로 pypy3로 제출

R, C = map(int, input().split()) # R이 세로, C가 가로

graph = [list(input().strip()) for _ in range(R)]
max_cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x, cur_cnt, alphabets):
    global max_cnt
    max_cnt = max(max_cnt, cur_cnt)

    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]

        if 0 <= next_y < R and 0 <= next_x < C:
            next_alphabet = graph[next_y][next_x]

            if next_alphabet not in alphabets:
                alphabets.add(next_alphabet)
                dfs(next_y, next_x, cur_cnt+1, alphabets)
                alphabets.remove(next_alphabet) # 백트래킹 : 다음 경로를 찾기위해 알파벳 제거

start_alphabets = set(graph[0][0])
dfs(0, 0, 1, start_alphabets)
print(max_cnt)