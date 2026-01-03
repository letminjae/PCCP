# 9663 - N-Queen
# 속도를 위해 pypy3으로 제출

import sys
input = sys.stdin.readline

N = int(input())
answer = 0
# 한 행에는 어차피 퀸이 1개만 올 수 있음
rows = [0]*N

def is_valid(n):
    for i in range(n):
        # 같은 열에 퀸이 있거나, 대각선에 퀸이 있는 경우
        if rows[n] == rows[i] or abs(rows[n] - rows[i]) == abs(n - i):
            return False
    return True

def dfs(row):
    global answer
    
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        rows[row] = col
        if is_valid(row):
            dfs(row+1)
            
dfs(0)
print(answer)