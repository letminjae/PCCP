# 1010 다리놓기

TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    a, b = 1, 1

    for i in range(M-N+1,M+1):
        a = a * i

    for j in range(1, N+1):
        b = b * j

    print(int(a / b))