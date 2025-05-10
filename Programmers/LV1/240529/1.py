# 푸드 파이트 대회

def solution(food):
    fight = ''
    for i in range(1, len(food)):
        fight += str(i) * (food[i] // 2)
    return fight + '0' + fight[::-1]

print(solution([1, 7, 1, 2]))