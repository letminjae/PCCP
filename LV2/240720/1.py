# 압축

def solution(msg):
    answer = []

    dic = {chr(i+64): i for i in range(1,27)}

    start = end = 0
    while (True):
        end += 1
        print(f'start={start}, end={end}')

        if end == len(msg):
            answer.append(dic[msg[start:end]])
            break
        
        # 없는 글자는 dict에 추가해야함
        if msg[start:end+1] not in dic:
            dic[msg[start:end+1]] = len(dic) + 1
            answer.append(dic[msg[start:end]])
            start = end	# start를 다음글자로 옮긴다
            
        print(f'answer={answer}')
    return answer

print(solution("KAKAO"))