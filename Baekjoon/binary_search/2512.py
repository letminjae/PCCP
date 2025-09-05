# 2512 - 예산

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

answer = 0

# 예산이 많아서 다 줄 수 있는경우
if sum(arr) <= budget:
    print(max(arr))
else:
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2 # 예산의 상한선
        total = 0 # 총 예측 예산
        for request in arr:
            if request > mid:
                total += mid
            else:
                total += request
            
        # 예측 예산이 실 예산보다 작으면 정답이 되고, 더 큰값을 찾아본다.
        if total <= budget:
            answer = mid
            start = mid + 1
        # 예측 예산보다 실 예산이 크면 불가, 상한선을 줄인다.
        else:
            end = mid - 1

    print(answer)