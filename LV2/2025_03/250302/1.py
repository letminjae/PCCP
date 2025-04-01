# 2 * N 타일링

# 피보나치 수열
# n이 1일 때, 1개의 경우의 수
# n이 2일 때, 2개의 경우의 수
# n이 3일 때, 3개의 경우의 수
# n이 4일 때, 5개의 경우의 수
# n이 5일 때, 8개의 경우의 수 ... f(n) = f(n-1) + f(n-2)의 형태, 단 f(1) = 1, f(2) = 2

def solution(n):
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b % 1000000007

solution(4) # 5