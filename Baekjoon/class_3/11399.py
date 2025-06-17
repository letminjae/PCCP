# 11399 ATM

import sys
input = sys.stdin.readline

N = int(input())

spend_time = sorted(list(map(int, input().split())))

answer = [spend_time[0]]

for i in range(1, N):
    answer.append(answer[i-1] + spend_time[i])

print(sum(answer))