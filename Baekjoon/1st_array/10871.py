# 10871 X보다 작은 수

N, X = map(int, input().split())
lst = list(map(int,input().split()))

answer = []

for num in lst:
    if num < X:
        answer.append(str(num))

print(' '.join(answer))