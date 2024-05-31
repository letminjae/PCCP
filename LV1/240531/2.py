# 과일 장수

def solution(k, m, score):
    answer = 0
    SortedScore = sorted(score, reverse=True)
    if len(SortedScore) % m != 0:
        SortedScore = SortedScore[:len(SortedScore) - len(SortedScore) % m]

    box = []
    for i in range(0, len(SortedScore), m):
        box.append(SortedScore[i:i + m])

    for i in box:
        price = min(i)*len(i)
        answer += price
    return answer
