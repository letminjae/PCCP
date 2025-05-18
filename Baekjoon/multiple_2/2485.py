# 2485 가로수

import math

N = int(input())
trees = [int(input()) for _ in range(N)]

diffs = [trees[i+1] - trees[i] for i in range(N-1)]

gcd = diffs[0]
for d in diffs[1:]:
    gcd = math.gcd(gcd, d) # 간격마다 최대공약수 갱신 

answer = 0

for d in diffs:
    answer += (d // gcd) - 1
    
print(answer)