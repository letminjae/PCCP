# 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    PS = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for personal, choice in zip(survey, choices):
        if choice > 4:
            PS[personal[1]] += choice-4
        elif choice < 4:
            PS[personal[0]] += 4-choice
    
    li = list(PS.items())

    for i in range(0, 8, 2):
        if li[i][1] < li[i+1][1]:
            answer += li[i+1][0]
        else:
            answer += li[i][0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))