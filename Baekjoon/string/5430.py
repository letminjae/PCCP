# 5430 - AC (골드5)

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    # 데이터 파싱
    func = input().strip() # 실행할 함수
    arr_len = int(input()) # 배열의 길이
    raw_arr_data = input().strip() # "[1,2,3,4]"

    if arr_len == 0:
        q = deque()
    else:
        q = deque(raw_arr_data[1:-1].split(','))
        
    # 처리 시작
    # R이 나올때 마다 뒤집으면 연산이 많아져 Flag 사용
    is_reversed = False
    is_error = False
    
    for f in func:
        # R일 때 뒤집기
        if f == "R":
            is_reversed = not is_reversed # Toggle 기법
        # D일 때 하나빼기
        else:
            if not q:
                is_error = True
                break
            
            if not is_reversed:
                q.popleft()
            else:
                q.pop()
    
    if is_error:
        print("error")
    else:
        if is_reversed:
            q.reverse()
        print("[" + ",".join(q) + "]")