# 2108 통계학

import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())

numbers = [int(input()) for _ in range(N)]
counter = Counter(numbers)

def custom_round(n):
    return int(n + 0.5) if n > 0 else int(n - 0.5)

print(custom_round(sum(numbers)/N))

numbers.sort()
print(numbers[N//2])

max = max(counter.values())
modes = [num for num, count in counter.items() if count == max]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])

print(numbers[-1] - numbers[0])