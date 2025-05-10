# 배열의 원소만큼 추가하기

def solution(arr):
    answer = []
    for i in arr:
        for j in range(1,i+1):
            answer.append(i)
    return answer

print(solution([5, 1, 4]))