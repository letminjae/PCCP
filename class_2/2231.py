# 2231 분해합

N = int(input())
answer = 0

for i in range(1, N+1):
    lst = list(map(int, str(i)))
    sum_list = i + sum(lst)
    if sum_list == N:
        answer = i
        break
    if i == N:
        answer = 0

print(answer)