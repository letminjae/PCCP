# 3052 나머지

arr = []
for _ in range(10):
    n = int(input())
    arr.append(n % 42)

arr = set(arr)
print(len(arr))