# 14888 - 연산자 끼워넣기
# 순열버전

import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
S = list(map(str, input().split()))
calc_num = list(map(int, input().split()))
calc = []

while sum(calc_num) > 0:
    if calc_num[0] > 0:
        calc.append('+')
        calc_num[0] -= 1
    elif calc_num[1] > 0:
        calc.append('-')
        calc_num[1] -= 1
    elif calc_num[2] > 0:
        calc.append('*')
        calc_num[2] -= 1
    else:
        calc.append('//')
        calc_num[3] -= 1

max_val = -float('inf')
min_val = float('inf')

for p in set(permutations(calc, len(calc))):
    res = int(S[0])

    for i in range(len(p)):
        num = int(S[i+1])
        op = p[i]

        if op == '+':
            res += num
        elif op == '-':
            res -= num
        elif op == '*':
            res *= num
        else:
            if res < 0:
                res = -(-res//num)
            else:
                res //= num
    
    max_val = max(max_val, res)
    min_val = min(min_val, res)

print(max_val)
print(min_val)