# 30802 웰컴 키트

import math

N = int(input())
tShirt = list(map(int, input().split()))
T, P = map(int, input().split())

sum_t = 0
for t in tShirt:
    sum_t += math.ceil(t / T)

print(sum_t)
print(N // P, N % P)