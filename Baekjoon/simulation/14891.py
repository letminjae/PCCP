# 14891 - 톱니바퀴 (골드5)

import sys
input = sys.stdin.readline
from collections import deque

# 톱니바퀴 4개
q = deque([])
for _ in range(4):
    q.append(deque(list(map(int, input().strip()))))

# 회전하려는 횟수
K = int(input())

# 연쇄 회전(오른쪽)
def check_right(idx, dir):
    if idx > 3:
        return
    
    if q[idx-1][2] != q[idx][6]:
        rotations[idx] = -dir
        check_right(idx+1, -dir)

# 연쇄 회전(왼쪽)
def check_left(idx, dir):
    if idx < 0:
        return
    
    if q[idx+1][6] != q[idx][2]:
        rotations[idx] = -dir
        check_left(idx-1, -dir) 

# 회전 시작
for _ in range(K):
    # 톱니바퀴 번호, 회전방향
    number, direction = map(int, input().split())

    target = number-1 # 인덱스 보정

    rotations = [0]*4
    rotations[target] = direction

    check_left(target-1, direction)
    check_right(target+1, direction)

    for i in range(4):
        if rotations[i] != 0:
            q[i].rotate(rotations[i])

answer = 0

# N극은 0, S극은 1
for i in range(4):
    if q[i][0] == 1:
        answer += 2**i

print(answer)