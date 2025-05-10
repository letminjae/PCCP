# 카펫

def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            x = yellow // i
            y = i
            if x*2 + y*2 + 4 == brown:
                answer.append(x+2)
                answer.append(y+2)
                break
            answer.sort(reverse = True)
    return answer