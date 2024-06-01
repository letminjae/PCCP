# 실패율

def solution(N, stages):
    answer = []
    fail = {}
    players = len(stages)

    for i in range(1,N+1):
        if players == 0:
            fail[i] = 0
        else:
            fail[i] = stages.count(i)/players
            players = players - stages.count(i)
    
    answer = sorted(fail, key=lambda x : fail[x],reverse=True)

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))