# 대충 만든 자판

def solution(keymap, targets):
    answer = []

    for target in targets:
        count = 0
        for char in target:
            # flag = key에 원하는 문자가 있는지 없는지 확인
            flag = False
            # time = keymap의 최대 원소가 100개
            time = 101
            for key in keymap:
                if char in key:
                    time = min(key.index(char)+1, time)
                    flag = True
            if not flag:
                count = -1
                break
            count += time
        answer.append(count)
   
    return answer