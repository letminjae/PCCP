# 10815 숫자카드

from collections import Counter

N = int(input())
card = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

count = Counter(card)

for number in target:
    if count[number] == 1:
        print("1", end=" ")
    else:
        print("0", end=" ")