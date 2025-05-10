# 튜플

def solution(s):
    answer = []
    l = []
    for i in s.split('},'):
        l.append(i.replace("{","").replace("}","").split(","))
    l.sort(key=len)

    for i in l:
        for j in i:
            if j not in answer:
                answer.append(j)

    return list(map(int,answer))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))