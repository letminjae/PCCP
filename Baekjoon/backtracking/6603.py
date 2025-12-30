# 6603 - 로또

import sys
input = sys.stdin.readline

def dfs(arr, lotto, index, depth):

    if depth == 6:
        print(*arr)
        return

    for i in range(index, len(lotto)):
        arr[depth] = lotto[i]
        dfs(arr, lotto, i+1, depth+1)


while True:
    lotto = list(map(int, input().split()))

    if lotto[0] == 0:
        break

    arr = [0]*6

    dfs(arr, lotto[1:], 0, 0)

    print()