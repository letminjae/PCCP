# 1316 그룹단어체커 - 실버5

N = int(input())

count = N

for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            count -= 1
            break

print(count)