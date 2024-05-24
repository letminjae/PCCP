# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer
