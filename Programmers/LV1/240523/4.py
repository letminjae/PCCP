# 체육복

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 도난당했는데, 여벌 있는 학생 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복을 빌릴 수 있는 사람
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)