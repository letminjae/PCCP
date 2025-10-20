# 1541 잃어버린 괄호

import sys
input = sys.stdin.readline

N = input().split('-')
arr = []

for i in N:
    sum = 0
    number = i.split('+')
    for j in number:
        sum += int(j)
    arr.append(sum)

answer = arr[0]

for i in range(1, len(arr)):
    answer -= arr[i]

print(answer)