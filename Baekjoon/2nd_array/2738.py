# 2738 행렬 덧셈

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = " ")
    print()