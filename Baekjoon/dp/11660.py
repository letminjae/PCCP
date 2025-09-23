# 11660 - 구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

prefix_sum = [[0]*(N+1) for _ in range(N+1)]
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        # 윗부분 누적합 + 왼쪽 누적합 - 대각선 누적합
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # (1,1)~(x2,y2) 직사각형 값에서 원하지 않는 부분을 뺀다. (x1-1, y1-1은 2번 빠졌기에 1번 더함)
    sum = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

    print(sum)