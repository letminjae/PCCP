# 30804 과일 탕후루

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0
count = {}
fruits_count = 0
left = 0

for i in range(N):
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1
        fruits_count += 1

    while fruits_count > 2:
        count[arr[left]] -= 1
        
        if count[arr[left]] == 0:
            del(count[arr[left]])
            fruits_count -= 1
        left += 1
    
    answer = max(answer, i-left+1)

print(answer)