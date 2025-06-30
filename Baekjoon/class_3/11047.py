# 11047 동전 0

import sys
input = sys.stdin.readline
coin, money = map(int, input().split())

coin_list = sorted([int(input()) for _ in range(coin)], reverse=True)

answer = 0

for c in coin_list:
    if money >= c:
        answer += money // c
        money %= c
        if money <= 0:
            break

print(answer)