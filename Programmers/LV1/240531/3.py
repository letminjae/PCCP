# 소수찾기

# 효율성 탈락해서 다시 품
def solution(n):
    answer = 0
    for i in range(2, n+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            print(f'i={i}, j={j}')
            print(i % j == 0)
            if i % j == 0:
                count += 1
            if count == 2:
                break
        if count == 1:
            answer += 1
    return answer

print(solution(10))