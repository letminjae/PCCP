# 가장 가까운 같은 글자

def solution(s):
    answer = []
    word = dict()
    for i, v in enumerate(s):
        if v not in word:
            answer.append(-1)
        else:
            answer.append(i - word[v])
        word[v] = i
    return answer
