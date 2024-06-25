# 멀리 뛰기

# 피보나치 수열 사용

def solution(n):
    answer = [0] * (n+1)
    answer[0] = 1
    answer[1] = 2

    for i in range(2, n+1):
        answer[i] = answer[i-2] + answer[i-1]
   
    return answer[n-1] % 1234567

print(solution(3))