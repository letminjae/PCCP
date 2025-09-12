# 프로그래머스 LV3 - 거스름돈


def solution(n, money):
    answer = 0

    dp = [1] + [0]*n

    for coin in money:
        # 1 2 5
        for i in range(coin, n+1):
            dp[i] = dp[i] + dp[i-coin]

    answer = dp[-1]
    return answer % 1000000007

solution(5, [1,2,5])