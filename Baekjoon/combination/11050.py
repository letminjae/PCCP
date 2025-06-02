# 11050 이항 계수 1

M, N = map(int, input().split())

a, b = 1, 1

for i in range(M-N+1,M+1):
    a = a * i

for j in range(1, N+1):
    b = b * j

print(int(a / b))