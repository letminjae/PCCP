# 15552 빠른 A+B

from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    a, b = map(int, stdin.readline().split())
    print(a+b)
