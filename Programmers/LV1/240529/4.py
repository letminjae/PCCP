# 추억 점수

def solution(name, yearning, photo):
    answer = []
    dic = dict()
   
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for friends in photo:
        score = 0
        for i in range(len(friends)):
            if friends[i] in dic:
                score += dic[friends[i]]

        answer.append(score)

    return answer