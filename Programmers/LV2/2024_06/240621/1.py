# 점프와 순간 이동

def solution(n):
    cnt = 0
    if n == 1:
        return 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        if n % 2 == 1:
            n = n - 1
            cnt += 1
    return cnt

#bin을 이용한 풀이
#def solution(n):
#    return bin(n).count('1')