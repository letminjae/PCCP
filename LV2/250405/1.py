# 시소 짝꿍

# def solution(weights):
#     answer = 0
#     weights.sort() # 100 100 180 270 360
#     for i in range(len(weights)):
#         for j in range(i + 1, len(weights)):
#           if weights[i] == weights[j]:
#             answer += 1
#           elif weights[i] * 2 == weights[j] * 3:
#             answer += 1
#           elif weights[i] * 3 == weights[j] * 2:
#             answer += 1
#           elif weights[i] * 2 == weights[j] * 4:
#             answer += 1
#           elif weights[i] * 4 == weights[j] * 2:
#             answer += 1
#           elif weights[i] * 3 == weights[j] * 4:
#             answer += 1
#           elif weights[i] * 4 == weights[j] * 3:
#             answer += 1

#     return answer

'''
- 카운터로 비교
몸무게 비율은 다음 4가지 경우만 존재함
1:1 (같은 무게)
2:3
2:4 → 1:2
3:4
'''

from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    ratio = [(1, 1), (2, 3), (1, 2), (3, 4)]
    
    for weight in counter:
        for x, y in ratio:
          target = weight * y / x
          if target in counter:
            if x == y: # 1:1, nC2
              answer += counter[weight] * (counter[weight] -1) // 2
            else:
              answer += counter[weight] * counter[target]
    
    return answer
solution([100, 180, 360, 100, 270]) # 4