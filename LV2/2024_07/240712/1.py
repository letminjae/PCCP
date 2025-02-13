# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tired = k
        cnt = 0

        for need, spend in p:
            if tired >= need:
                tired -= spend
                cnt += 1
            answer = max(answer, cnt)
    return answer
                

print(solution(80,[[80,20],[50,40],[30,10]]))