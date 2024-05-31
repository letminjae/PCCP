# 소수만들기

import itertools

def solution(nums):
    answer = 0
    nCr = list(itertools.combinations(nums, 3))
    numbers = [sum(i) for i in nCr]
    
    for i in numbers:
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                count += 1
                if count == 2:
                    break
        if count == 1:
            answer += 1
    return answer

print(solution([1,2,3,4]))