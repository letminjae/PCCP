# 양궁대회

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    info_size = len(info)
    prev_score_diff = 0

    for comb in combinations_with_replacement(range(info_size), n):
        rion_info = [0]*info_size
        rion_score = 0
        apeach_score = 0

        # 라이언이 쏠 수 있는 모든 경우의 수 - 중복조합
        for idx in comb:
            rion_info[idx] += 1
        rion_info = rion_info[::-1]
        
        # 둘의 점수 비교
        for number in range(info_size):
            if rion_info[number] > info[number]:
                rion_score += 10-number
            elif info[number]:
                apeach_score += 10-number
        
        # 점수차가 이전 점수 차보다 크다면, 이전점수 갱신
        score_diff = rion_score - apeach_score
        if score_diff > prev_score_diff:
            prev_score_diff = score_diff
            answer = rion_info

    return answer
    

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
# [0,2,2,0,1,0,0,0,0,0,0]