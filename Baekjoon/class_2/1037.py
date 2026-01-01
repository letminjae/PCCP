# 1037 약수

N = int(input())

A = list(map(int, input().split()))

max = max(A)
min = min(A)

print(max * min)