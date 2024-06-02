# 다트게임 - 2018 카카오 블라인드 코딩테스트

def solution(dartResult):
    n = ''
    result = []

    # S,D,T 점수 계산
    for i in dartResult:
        if i.isdigit():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            result.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            result.append(n)
            n = ''  
        elif i == 'T':
            n = int(n) ** 3
            result.append(n)
            n = ''
        # *, # 점수 계산
        elif i == '*':
            if len(result) > 1:
                result[-2] = result[-2] * 2
                result[-1] = result[-1] * 2
            else:
                result[-1] = result[-1] * 2
        elif i == '#':
            result[-1] = result[-1] * -1

    return sum(result)

print(solution('1S2D*3T'))