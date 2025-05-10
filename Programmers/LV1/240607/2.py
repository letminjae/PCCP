# 신규 아이디 추천

def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    # 2
    for char in new_id:
        if char.isalnum() or char in '-_.':
            answer += char
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:]
    else: 
        answer = answer
    if answer[-1] == '.':
        answer = answer[:-1]
    else:
        answer = answer
    # 5
    if answer == '':
        answer += "a"
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))