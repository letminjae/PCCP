# 11650 좌표 정렬하기

N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort(key=lambda x:(x[0],x[1]))

for num in arr:
    x, y = num[0], num[1]
    print(x, y)