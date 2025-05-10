# 모의고사

def solution(answers):
    answer = [0 for i in range(3)]
   
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            answer[0] += 1
        if answers[i] == student2[i%len(student2)]:
            answer[1] += 1
        if answers[i] == student3[i%len(student3)]:
            answer[2] += 1

    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i+1)

    return sorted(result)
