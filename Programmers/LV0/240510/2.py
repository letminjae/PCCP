# 옹알이 (1)

def solution(babbling):
    correct = ["aya","ye","woo","ma"]
    answer = 0
   
    for babble in babbling:
        result = 0
        for j in range(len(correct)):
            if babble.find(correct[j]) != -1:
                result += len(correct[j])
        if len(babble) == result:
            answer += 1
   
    return answer