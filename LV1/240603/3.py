# 짝꿍 게임

from collections import Counter

def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)
    print(X, Y)

    answer = ''
    for i in range(10):
        answer += str(i) * min(X[str(i)], Y[str(i)])

    if answer == '':
        return '-1'
    
    answer = ''.join(sorted(answer, reverse=True))
    if answer[0] == '0':
        return '0'
    else:
        return answer

print(solution("100","123450"))