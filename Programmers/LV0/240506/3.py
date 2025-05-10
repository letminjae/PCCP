# 무작위로 k개의 수 뽑기

def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer and len(answer) < k:
            answer.append(num)
    return answer + [-1] * (k - len(answer))

print(solution([0, 1, 1, 1, 1],4))