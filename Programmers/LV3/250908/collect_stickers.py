# 프로그래머스 LV3 - 스티커 모으기 2 (collect_stickers.py)
# 동적 계획법 (DP) - 최대 합 기록

def solution(sticker):
    N = len(sticker)

    if N == 1:
        return sticker.pop()

    dp_1 = [0] + sticker[:-1]
    dp_2 = [0] + sticker[1:]

    # 첫번째 스티커를 떼는 경우
    for i in range(2, N):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2]+dp_1[i])

    # 첫번째 스티커를 떼지 않는 경우
    for i in range(2, N):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2]+dp_2[i])

    return max(dp_1[-1], dp_2[-1])

solution([14, 6, 5, 11, 3, 9, 2, 10])