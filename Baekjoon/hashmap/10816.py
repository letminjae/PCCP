# 10816 숫자카드 2

from collections import Counter

N = int(input())
dict_N = dict(Counter(map(int, input().split())))
M = int(input())
question = list(map(int, input().split()))

for num in question:
    if num in dict_N:
        print(dict_N[num], end=' ')
    else:
        print(0, end=' ')