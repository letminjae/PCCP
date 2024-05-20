# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    max_cnt = 0
    min_cnt = 0
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    for num in lottos:
        if num in win_nums:
            max_cnt += 1
            min_cnt += 1
        # 최고 등수 일 때
        if num == 0:
            max_cnt += 1

    # 등수 계산
    return [dic[max_cnt], dic[min_cnt]]