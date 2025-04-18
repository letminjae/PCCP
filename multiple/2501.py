# 2501 약수 구하기

a, b = map(int, input().split())

multiple = []

for i in range(1, a+1):
    if a % i == 0:
        multiple.append(i)

if len(multiple) < b:
    print(0)
else:
    print(multiple[b-1])