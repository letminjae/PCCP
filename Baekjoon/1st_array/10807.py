# 10807 개수 세기

N = int(input())
lst = list(input().split())
v = int(input())
count = 0

for num in lst:
    if v == int(num):
        count += 1

print(count)