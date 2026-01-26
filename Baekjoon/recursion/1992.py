# 1992 - 쿼드트리 (실버 1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
video = []

for _ in range(N):
    v = [int(i) for i in list(input().rstrip())]
    video.append(v)

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]])
    temp += quadtree(half,[l[half:] for l in vlist[:half]])
    temp += quadtree(half,[l[:half] for l in vlist[half:]])
    temp += quadtree(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

print(quadtree(N, video))