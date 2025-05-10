# 11478 서로 다른 부분 문자열의 개수

N = input()

cnt = 1
answer = []

for i in range(len(N)):
    answer.append(N[i])

while cnt < len(N):
    for i in range(len(N)-cnt):
        answer.append(N[i:i+cnt+1])
    cnt += 1

answer = set(answer)

print(len(answer))