# 25192 인사성 밝은 곰곰이

import sys
input = sys.stdin.readline

N = int(input())
answer = 0
set_user = set()

for _ in range(N):
    user = input().strip()
    if user == "ENTER":
        answer += len(set_user)
        set_user = set()
    else:
        set_user.add(user)

answer += len(set_user)

print(answer)