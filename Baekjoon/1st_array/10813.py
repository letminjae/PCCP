# 10813 공 바꾸기

N, M = map(int, input().split())
arr = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
  
print(*arr[1:])