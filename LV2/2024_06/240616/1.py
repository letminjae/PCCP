# 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            print(f'i={i}, j={j}')
            sum += j
            print(f'sum={sum}')
            if sum == n:
                answer += 1
            elif sum > n :
                break
    return answer

print(solution(15))