# 스킬트리

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        print(skill_tree)
        queue = deque(skill)
        flag = True

        for str in skill_tree:
            print('str', str)
            # 큐에 선행스킬이 없으면 넘어감
            if str not in queue:
                print("continue")
                continue
            # 큐에 선행스킬이 있으면 하나씩 선행스킬을 지우고, 안 맞으면 False 후 Break
            else:
                if str == queue[0]:
                    print("str, queue0", str, queue[0])
                    queue.popleft()
                else:
                    print("flag False")
                    flag = False
                    break
        if flag:
            answer += 1
            print(answer)

    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])