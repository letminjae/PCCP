# 프로그래머스 LV3 - 입국심사
# 이분탐색 문제

def solution(n, times):
    answer = 0
    
    start = 1
    end = max(times) * n
    
    # start와 end가 같아지는 지점을 찾으면 정답 최솟값
    while start < end:
        mid = (start + end) // 2
        
        # 중앙값 기준으로 총 몇명을 심사할 수 있을지 구한다.
        total_people = 0
        for t in times:
            total_people += mid // t
            
        # 명수가 크면, 충분히 심사가능하니 끝 값을 반으로 만든다.
        if total_people >= n:
            end = mid
        # 명수가 작으면, 심사가 불가하니 앞의 값을 늘린다.
        else:
            start = mid + 1
    
    answer = start
    return answer

solution(6, [7, 10]) # 28