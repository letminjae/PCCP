# 2798 블랙잭

from itertools import combinations

N, M = map(int, input().split())

lst = list(map(int, input().split()))
combi_sum = [sum(num) for num in list(combinations(lst, 3))]
combi_sum = [num for num in combi_sum if num <= M]
combi_sum.sort(reverse=True)

print(combi_sum[0])