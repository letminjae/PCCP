# 25304 영수증

receipt = int(input())
count = int(input())

sum = 0
for _ in range(count):
    a, b = map(int, input().split())
    sum += a * b

if sum == receipt:
    print("Yes")
else:
    print("No")