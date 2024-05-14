# 겹치는 선분의 길이

def solution(lines):
    answer = 0
    count = [0 for _ in range(200)]
    for line in lines:
        for i in range(line[0], line[1]):
            count[i + 100] += 1
    answer += count.count(2)
    answer += count.count(3)
    return answer