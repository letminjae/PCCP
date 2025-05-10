# 10810 공 넣기

N, M = map(int, input().split())

arr = [0] * N

for _ in range(M):
    i, j, k = map(int,input().split())
    for x in range(i, j+1):
        arr[x-1] = k

for x in range(N):
    print(arr[x], end=' ')