chess = [1, 1, 2, 2, 2, 8]

input_chess = list(map(int, input().split()))

for i in range(6):
    if input_chess[i] == chess[i]:
        print(0, end=' ')
    elif input_chess[i] < chess[i]:
        print(chess[i] - input_chess[i], end=' ')
    else:
        print(-1 * (input_chess[i] - chess[i]), end=' ')