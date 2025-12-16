# 3273 두 수의 합

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
two_sum = int(input())
answer = 0

left = 0
right = N-1

while left < right:
    temp = arr[left] + arr[right]
    if temp == two_sum:
        answer += 1
        left += 1
    elif temp > two_sum:
        right -= 1
    else:
        left += 1

print(answer)