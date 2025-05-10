# 11022 A+B-8

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')