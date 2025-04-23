# 1018 체스판 다시 칠하기

N, M = map(int, input().split())
board = [input() for _ in range(N)]

pattern = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

min_paint = 64

for j in range(N-7):
    for i in range(M-7):
        count = 0

        for row in range(8):
            for col in range(8):
                if board[j + row][i + col] != pattern[row][col]:
                    count += 1

        min_paint = min(min_paint, count, 64-count)

print(min_paint)