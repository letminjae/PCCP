# 두 개 뽑아서 더하기

def solution(numbers):
    combination = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            combination.append(numbers[i] + numbers[j])
    answer = sorted(list(set(combination)))
    return answer