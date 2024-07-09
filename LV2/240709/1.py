# 타겟 넘버 (필수로 다시 복습!)

# BFS 풀이
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        print(f'num={num}')
        tmp = []
        for parent in leaves:
            print(f'parent={parent}')
            tmp.append(parent + num)
            tmp.append(parent - num)
            print(f'tmp={tmp}')
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer