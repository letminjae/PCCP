# 연속된 부분 수열의 합 - 투 포인터 사용

def solution(sequence, k):
    left, right = 0, 0
    total = sequence[0] # 현재 부분합
    answer = (0, len(sequence)) # 시작 ~ 끝 인덱스

    while right < len(sequence):
        # 1번 조건 : k와 total이 같을 때 더 짧은구간 갱신
        if total == k:
            if (right - left) < (answer[1] - answer[0]): # 더 짧은 구간이라면??
                answer = (left, right)

        # 2번 조건 : total이 k보다 작거나, 같거나 클 때 비교
        if total < k:
            right += 1
            if right < len(sequence): # 배열 범위 넘지않기
                total += sequence[right]
        else:
            total -= sequence[left]
            left += 1
    
    return list(answer)

# solution([1, 2, 3, 4, 5],7) # [2, 3]
solution([1, 1, 1, 2, 3, 4, 5], 5) # [6, 6]