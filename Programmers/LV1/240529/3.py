# 명예의 전당 (1)

def solution(k, score):
    answer = []
    q = []
    for num in score:
        if len(q) < k:
            q.append(num)
        else:
            if num > min(q):
                q.remove(min(q))
                q.append(num)
        q.sort()
        answer.append(q[0])
    return answer