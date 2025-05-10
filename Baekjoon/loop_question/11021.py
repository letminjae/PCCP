# 11021 A+B-7

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')