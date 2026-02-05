# 11729 - 하노이 탑 이동 순서 (골드5)

import sys
input = sys.stdin.readline

N = int(input())

def hanoi(N, start, end, sub):
    if N == 1:
        print(start, end)
        return
    
    hanoi(N-1, start, sub, end)
    print(start, end)

    hanoi(N-1, sub, end, start)

print((2**N)-1)
hanoi(N, 1, 3, 2)