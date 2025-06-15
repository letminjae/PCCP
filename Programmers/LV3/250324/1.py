# 최고의 집합

def solution(n, s):
    answer = []

    # 최고의 집합 존재 X
    if n > s:
        return [-1]
    
    answer = [s // n for _ in range(n)]
    
    # 합 / 자연수 개수의 나머지 = 원소에 1 더해주기
    for i in range(s % n):
        answer[i] += 1
            
    answer.sort()

    return answer

solution(2,9) # [4, 5]