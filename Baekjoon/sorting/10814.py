# 10814 나이순 정렬

N = int(input())

arr = []

for _ in range(N):
    x, y = input().split()
    x = int(x)
    arr.append((x, y))

arr.sort(key=lambda x:x[0])

for x, y in arr:
    print(f'{x} {y}')