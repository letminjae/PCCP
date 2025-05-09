# 1620 나는야 포켓몬 마스터

N, M = map(int, input().split())

alphaDict = {}
numberDict = {}

for i in range(1, N+1):
    pokemon = input().strip()
    alphaDict[i] = pokemon
    numberDict[pokemon] = i

for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        print(alphaDict[int(quiz)])
    else:
        print(numberDict[quiz])