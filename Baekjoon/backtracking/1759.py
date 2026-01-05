# 1759 - 암호 만들기

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))

temp = []
mouem = {"a","e","i","o","u"}

def dfs(start):
    if len(temp) == L:
        mouem_count = 0
        jauem_count = 0
    
        for char in temp:
            if char in mouem:
                mouem_count += 1
            else:
                jauem_count += 1

        if mouem_count >= 1 and jauem_count >= 2:
            print(''.join(temp))
            return
    
    for i in range(start,C):
        temp.append(arr[i])
        dfs(i+1)
        temp.pop()

dfs(0)