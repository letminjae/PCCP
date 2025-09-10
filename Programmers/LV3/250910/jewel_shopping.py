# 프로그래머스 LV3 - 보석 쇼핑 (카카오 인턴십)
# 모든 종류 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
# 투 포인터, 슬라이딩 윈도우

def solution(gems):
    set_gems = set(gems)
    dict_gems = {}

    answer = []
    start = 0
    end = 0

    while end < len(gems):
        if gems[end] in dict_gems:
            dict_gems[gems[end]] += 1
        else:
            dict_gems[gems[end]] = 1

        # 최소 구간 찾기위해 start 늘려서 answer 저장
        while len(dict_gems) == len(set_gems):
            answer.append([start + 1, end + 1])
            
            dict_gems[gems[start]] -= 1
            
            if dict_gems[gems[start]] == 0:
                del dict_gems[gems[start]]
                
            start += 1

        end += 1
    
    # 구간의 길이가 가장 짧은 순서로 정렬
    answer.sort(key=lambda x: x[1]-x[0])
    return answer[0]

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])