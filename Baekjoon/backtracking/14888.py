# 14888 - 연산자 끼워넣기
# 백트래킹 버전

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -float('inf')
min_val = float('inf')

def dfs(depth, total, plus, minus, multiple, divide):
    global max_val, min_val

    # 종료 조건
    if depth == N:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    
    # 연산자가 남아있을 때는 진행
    if plus > 0:
        dfs(depth+1, total+nums[depth], plus-1, minus, multiple, divide)
    if minus > 0:
        dfs(depth+1, total-nums[depth], plus, minus-1, multiple, divide)
    if multiple > 0:
        dfs(depth+1, total*nums[depth], plus, minus, multiple-1, divide)
    if divide > 0:
        dfs(depth+1, int(total/nums[depth]), plus, minus, multiple, divide-1)

dfs(1, nums[0], add, sub, mul, div)

print(max_val)
print(min_val)