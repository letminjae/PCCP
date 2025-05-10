# 2562 최댓값

arr = []

for _ in range(9):
    num = int(input())
    arr.append(num)

print(max(arr))
print(arr.index(max(arr))+1)